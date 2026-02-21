"""
Content Marketing AX - Plugin Loader
Loads skills and commands from knowledge-work-plugins
"""
import os
import json
from pathlib import Path
from typing import Dict, List, Any


class PluginLoader:
    """Loads and manages plugins from the plugins directory"""

    def __init__(self, plugins_dir: str = None):
        if plugins_dir is None:
            # Default to plugins directory relative to project root
            project_root = Path(__file__).parent.parent
            plugins_dir = project_root / "plugins"

        self.plugins_dir = Path(plugins_dir)
        self._plugins_cache = {}
        self._skills_cache = {}
        self._commands_cache = {}

    def load_plugin(self, plugin_name: str) -> Dict[str, Any]:
        """Load a plugin's metadata"""
        if plugin_name in self._plugins_cache:
            return self._plugins_cache[plugin_name]

        plugin_path = self.plugins_dir / plugin_name
        manifest_path = plugin_path / ".claude-plugin" / "plugin.json"

        if not manifest_path.exists():
            raise ValueError(f"Plugin {plugin_name} not found")

        with open(manifest_path, 'r') as f:
            manifest = json.load(f)

        self._plugins_cache[plugin_name] = {
            "name": plugin_name,
            "manifest": manifest,
            "path": plugin_path
        }

        return self._plugins_cache[plugin_name]

    def load_skill(self, plugin_name: str, skill_name: str) -> str:
        """Load a skill's content (markdown file)"""
        cache_key = f"{plugin_name}:{skill_name}"
        if cache_key in self._skills_cache:
            return self._skills_cache[cache_key]

        plugin_path = self.plugins_dir / plugin_name
        skill_path = plugin_path / "skills" / skill_name / "SKILL.md"

        if not skill_path.exists():
            raise ValueError(f"Skill {skill_name} not found in plugin {plugin_name}")

        with open(skill_path, 'r') as f:
            content = f.read()

        self._skills_cache[cache_key] = content
        return content

    def load_command(self, plugin_name: str, command_name: str) -> str:
        """Load a command's content (markdown file)"""
        cache_key = f"{plugin_name}:{command_name}"
        if cache_key in self._commands_cache:
            return self._commands_cache[cache_key]

        plugin_path = self.plugins_dir / plugin_name
        command_path = plugin_path / "commands" / f"{command_name}.md"

        if not command_path.exists():
            raise ValueError(f"Command {command_name} not found in plugin {plugin_name}")

        with open(command_path, 'r') as f:
            content = f.read()

        self._commands_cache[cache_key] = content
        return content

    def list_skills(self, plugin_name: str) -> List[str]:
        """List all skills in a plugin"""
        plugin_path = self.plugins_dir / plugin_name / "skills"

        if not plugin_path.exists():
            return []

        skills = []
        for skill_dir in plugin_path.iterdir():
            if skill_dir.is_dir():
                skill_file = skill_dir / "SKILL.md"
                if skill_file.exists():
                    skills.append(skill_dir.name)

        return skills

    def list_commands(self, plugin_name: str) -> List[str]:
        """List all commands in a plugin"""
        plugin_path = self.plugins_dir / plugin_name / "commands"

        if not plugin_path.exists():
            return []

        commands = []
        for command_file in plugin_path.glob("*.md"):
            commands.append(command_file.stem)

        return commands

    def get_skill_summary(self, plugin_name: str, skill_name: str) -> Dict[str, str]:
        """Get skill metadata from frontmatter"""
        content = self.load_skill(plugin_name, skill_name)

        # Parse frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1].strip()
                lines = frontmatter.split('\n')
                metadata = {}
                for line in lines:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip()
                return metadata

        return {}

    def load_all_skills_for_agent(self, plugin_names: List[str], skill_names: List[str] = None) -> str:
        """
        Load multiple skills and combine them into a single context string
        for agent system prompts.

        Args:
            plugin_names: List of plugin names to load skills from
            skill_names: Optional list of specific skill names. If None, loads all.

        Returns:
            Combined skills content
        """
        combined = []

        for plugin_name in plugin_names:
            if skill_names:
                skills = skill_names
            else:
                skills = self.list_skills(plugin_name)

            for skill_name in skills:
                try:
                    content = self.load_skill(plugin_name, skill_name)
                    combined.append(f"\n--- {plugin_name}/{skill_name} Skill ---\n")
                    combined.append(content)
                except Exception as e:
                    print(f"Warning: Could not load skill {skill_name} from {plugin_name}: {e}")

        return "\n".join(combined)


# Global plugin loader instance
_plugin_loader = None

def get_plugin_loader() -> PluginLoader:
    """Get or create the global plugin loader instance"""
    global _plugin_loader
    if _plugin_loader is None:
        _plugin_loader = PluginLoader()
    return _plugin_loader
