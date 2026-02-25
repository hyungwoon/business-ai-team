#!/bin/bash
# Business AI Team - 글로벌 삭제 스크립트
# 사용법: ./uninstall.sh

set -euo pipefail

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

echo ""
echo "=========================================="
echo "  Business AI Team - 글로벌 삭제"
echo "=========================================="
echo ""

# 1. 에이전트 & 플러그인 삭제
if [[ -d "$INSTALL_DIR" ]]; then
    rm -rf "$INSTALL_DIR"
    info "에이전트 & 플러그인 삭제 완료: $INSTALL_DIR"
else
    warn "글로벌 설치를 찾을 수 없습니다: $INSTALL_DIR"
fi

# 2. 커맨드 삭제
for CMD in route.md ask.md team.md; do
    TARGET="$COMMANDS_DIR/$CMD"
    if [[ -f "$TARGET" ]]; then
        rm "$TARGET"
        info "커맨드 삭제: $CMD"
        # 백업 복원
        if [[ -f "${TARGET}.bak" ]]; then
            mv "${TARGET}.bak" "$TARGET"
            info "  백업 복원: ${CMD}.bak → $CMD"
        fi
    fi
done

# 3. 규칙 삭제
RULE="expert-routing.md"
TARGET="$RULES_DIR/$RULE"
if [[ -f "$TARGET" ]]; then
    rm "$TARGET"
    info "규칙 삭제: $RULE"
    if [[ -f "${TARGET}.bak" ]]; then
        mv "${TARGET}.bak" "$TARGET"
        info "  백업 복원: ${RULE}.bak → $RULE"
    fi
fi

echo ""
echo "=========================================="
echo -e "  ${GREEN}삭제 완료!${NC}"
echo "=========================================="
echo ""
echo "참고: business-ai-team/ 프로젝트 내 로컬 파일은 그대로 유지됩니다."
echo "재설치: ./install.sh"
echo ""
