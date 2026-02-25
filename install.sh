#!/bin/bash
# Business AI Team - 글로벌 설치 스크립트
# 사용법: git clone [repo] && cd business-ai-team && ./install.sh
#
# 설치 내용:
#   1. agents/ + plugins/ → ~/.claude/business-team/ (에이전트 & 스킬)
#   2. commands (route.md, ask.md, team.md) → ~/.claude/commands/ (슬래시 커맨드)
#   3. rules (expert-routing.md) → ~/.claude/rules/ (라우팅 규칙)
#
# 기존 파일이 있으면 .bak 백업 후 덮어씁니다.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
INSTALL_DIR="$CLAUDE_DIR/business-team"
COMMANDS_DIR="$CLAUDE_DIR/commands"
RULES_DIR="$CLAUDE_DIR/rules"

# 색상
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

info()  { echo -e "${GREEN}[INFO]${NC} $1"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

# 필수 디렉토리 확인
[[ -d "$SCRIPT_DIR/agents" ]] || error "agents/ 폴더를 찾을 수 없습니다. 프로젝트 루트에서 실행하세요."
[[ -d "$SCRIPT_DIR/plugins" ]] || error "plugins/ 폴더를 찾을 수 없습니다. 프로젝트 루트에서 실행하세요."

echo ""
echo "=========================================="
echo "  Business AI Team - 글로벌 설치"
echo "=========================================="
echo ""

# 1. 에이전트 & 플러그인 복사
info "에이전트 & 플러그인 설치 중..."

if [[ -d "$INSTALL_DIR" ]]; then
    warn "기존 설치 발견 → 제거 후 재설치합니다."
    rm -rf "$INSTALL_DIR"
fi

mkdir -p "$INSTALL_DIR"
cp -R "$SCRIPT_DIR/agents" "$INSTALL_DIR/agents"
cp -R "$SCRIPT_DIR/plugins" "$INSTALL_DIR/plugins"

AGENT_COUNT=$(find "$INSTALL_DIR/agents" -name "*.md" | wc -l | tr -d ' ')
SKILL_COUNT=$(find "$INSTALL_DIR/plugins" -name "SKILL.md" | wc -l | tr -d ' ')
info "  agents: ${AGENT_COUNT}개, skills: ${SKILL_COUNT}개 설치 완료"

# 2. 커맨드 복사
info "슬래시 커맨드 설치 중..."
mkdir -p "$COMMANDS_DIR"

for CMD in route.md ask.md team.md; do
    SRC="$COMMANDS_DIR/$CMD"
    if [[ -f "$SRC" ]]; then
        # 이미 동일한 파일이면 건너뛰기
        if diff -q "$SCRIPT_DIR/.claude/commands/$CMD" "$SRC" > /dev/null 2>&1; then
            info "  $CMD — 이미 최신 버전"
            continue
        fi
        warn "  $CMD 기존 파일 백업 → ${CMD}.bak"
        cp "$SRC" "${SRC}.bak"
    fi
    cp "$SCRIPT_DIR/.claude/commands/$CMD" "$COMMANDS_DIR/$CMD"
    info "  $CMD 설치 완료"
done

# 3. 규칙 복사
info "라우팅 규칙 설치 중..."
mkdir -p "$RULES_DIR"

RULE="expert-routing.md"
SRC="$RULES_DIR/$RULE"
if [[ -f "$SRC" ]]; then
    if diff -q "$SCRIPT_DIR/.claude/rules/$RULE" "$SRC" > /dev/null 2>&1; then
        info "  $RULE — 이미 최신 버전"
    else
        warn "  $RULE 기존 파일 백업 → ${RULE}.bak"
        cp "$SRC" "${SRC}.bak"
        cp "$SCRIPT_DIR/.claude/rules/$RULE" "$RULES_DIR/$RULE"
        info "  $RULE 설치 완료"
    fi
else
    cp "$SCRIPT_DIR/.claude/rules/$RULE" "$RULES_DIR/$RULE"
    info "  $RULE 설치 완료"
fi

# 완료
echo ""
echo "=========================================="
echo -e "  ${GREEN}설치 완료!${NC}"
echo "=========================================="
echo ""
echo "설치 경로:"
echo "  에이전트/스킬: $INSTALL_DIR/"
echo "  커맨드:       $COMMANDS_DIR/{route,ask,team}.md"
echo "  규칙:         $RULES_DIR/expert-routing.md"
echo ""
echo "사용법:"
echo "  어떤 프로젝트에서든 다음 커맨드를 사용할 수 있습니다:"
echo "    /route [비즈니스 요청]  — 전문가 라우팅"
echo "    /ask [질문]            — 간편 전문가 질문"
echo "    /team                  — 팀 목록 확인"
echo ""
echo "삭제: ./uninstall.sh"
echo ""
