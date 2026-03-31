import { readFile, writeFile } from 'node:fs/promises'
import { join } from 'node:path'
import { glob } from 'node:fs/promises'

const PLUGINS_DIR = '/Users/hyungwoon/Documents/AI/_core/business-ai-team/plugins'

async function findSkillFiles(): Promise<string[]> {
  const files: string[] = []
  for await (const entry of glob(`${PLUGINS_DIR}/*/skills/*/SKILL.md`)) {
    files.push(entry)
  }
  return files.sort()
}

function extractWhenToUse(description: string, skillName: string, pluginName: string): string {
  // Many descriptions already have "Use when ..." or "Trigger with ..." — extract that portion
  const useWhenMatch = description.match(/(?:Use when|Trigger with|Triggers?\s+(?:with|on|when))[^.]*(?:\.[^.]*)*$/i)
  if (useWhenMatch) {
    return useWhenMatch[0].trim()
  }

  // "Use when" pattern anywhere in the string
  const useWhenIdx = description.search(/use when/i)
  if (useWhenIdx !== -1) {
    return description.slice(useWhenIdx).trim()
  }

  // Fallback: generate from skill name and plugin
  const skill = skillName.replace(/-/g, ' ')
  const plugin = pluginName.replace(/-/g, ' ')
  return `${plugin} 도메인에서 ${skill} 작업이 필요할 때 사용`
}

function buildNewFrontmatter(
  existingFields: string,
  whenToUse: string
): string {
  // Escape double quotes in whenToUse
  const safe = whenToUse.replace(/"/g, "'")
  const newFields = [
    `when_to_use: "${safe}"`,
    `allowed-tools: [Read, Glob, Grep, WebSearch, WebFetch]`,
  ]
  return existingFields.trimEnd() + '\n' + newFields.join('\n') + '\n'
}

async function processFile(filePath: string): Promise<{ path: string; status: 'skipped' | 'updated' }> {
  const content = await readFile(filePath, 'utf-8')

  // Check for existing when_to_use (already processed)
  if (content.includes('when_to_use:')) {
    return { path: filePath, status: 'skipped' }
  }

  // Ensure file starts with frontmatter
  if (!content.startsWith('---')) {
    return { path: filePath, status: 'skipped' }
  }

  // Find closing --- of frontmatter
  const afterOpen = content.slice(3)
  const closingIdx = afterOpen.indexOf('\n---')
  if (closingIdx === -1) {
    return { path: filePath, status: 'skipped' }
  }

  const frontmatterBody = afterOpen.slice(0, closingIdx + 1) // includes leading \n
  const rest = afterOpen.slice(closingIdx + 4) // after \n---

  // Extract description value (may be multi-line with quotes)
  const descMatch = frontmatterBody.match(/^description:\s*["']?(.*?)["']?\s*$/m)
  const description = descMatch ? descMatch[1] : ''

  // Extract plugin and skill names from path
  // Path pattern: .../plugins/<plugin>/skills/<skill>/SKILL.md
  const parts = filePath.split('/')
  const skillsIdx = parts.lastIndexOf('skills')
  const pluginName = skillsIdx > 0 ? parts[skillsIdx - 1] : 'unknown'
  const skillName = skillsIdx > 0 ? parts[skillsIdx + 1] : 'unknown'

  const whenToUse = extractWhenToUse(description, skillName, pluginName)
  const newFrontmatterBody = buildNewFrontmatter(frontmatterBody, whenToUse)
  const newContent = '---\n' + newFrontmatterBody + '---' + rest

  await writeFile(filePath, newContent, 'utf-8')
  return { path: filePath, status: 'updated' }
}

async function main() {
  const files = await findSkillFiles()
  console.log(`Found ${files.length} SKILL.md files`)

  let updated = 0
  let skipped = 0
  const errors: string[] = []

  for (const file of files) {
    try {
      const result = await processFile(file)
      if (result.status === 'updated') {
        updated++
        console.log(`  [updated] ${file.replace(PLUGINS_DIR + '/', '')}`)
      } else {
        skipped++
      }
    } catch (err) {
      errors.push(`${file}: ${err}`)
    }
  }

  console.log(`\nDone: ${updated} updated, ${skipped} skipped, ${errors.length} errors`)
  if (errors.length > 0) {
    console.error('Errors:')
    errors.forEach(e => console.error(' ', e))
  }
}

main().catch(err => {
  console.error('Fatal:', err)
  process.exit(1)
})
