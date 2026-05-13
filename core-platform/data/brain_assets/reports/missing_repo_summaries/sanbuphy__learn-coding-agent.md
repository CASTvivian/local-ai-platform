# Missing Repo Summary Source: sanbuphy/learn-coding-agent

- URL: https://github.com/sanbuphy/learn-coding-agent
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/sanbuphy__learn-coding-agent
- Clone Status: cloned
- Language: None
- Stars: 11845
- Topics: 
- Description: Research on Coding Agents

## Extracted README / Docs / Examples



# FILE: README_JA.md

# Claude Code アーキテクチャ学習と研究

> **はじめに**: このプロジェクトは、CLI Agent アーキテクチャに関する学習および研究用のリポジトリです。すべての資料は、インターネット上で公開されている情報や議論のみに基づいてまとめられており、特に現在非常に人気のある CLI Agent `claude-code` に関する公開情報を参考にしています。私たちの目的は、開発者が Agent 技術をより深く理解し、活用できるように支援することです。今後も Agent アーキテクチャに関する洞察や実践的な議論を継続的に共有していく予定です。皆様のご関心とご支援に感謝いたします！

> **免責事項**: 本リポジトリのコンテンツは技術研究、学習、教育目的の交流のためにのみ提供されます。**商用利用は厳禁です。** いかなる個人、機関、団体も、本コンテンツを商業目的、営利活動、違法行為、その他の無許可の用途に使用することはできません。本コンテンツがお客様の法的権利、知的財産権、その他の利益を侵害する場合は、ご連絡いただければ直ちに確認・削除いたします。


**言語**: [English](README.md) | [中文](README_CN.md) | [한국어](README_KR.md) | **日本語**

---

## ツールシステムと権限アーキテクチャ

```text
                    ツールインターフェース
                    ==============

    buildTool(definition) ──> Tool<Input, Output, Progress>

    各ツールは以下を実装します:
    ┌────────────────────────────────────────────────────────┐
    │  ライフサイクル (LIFECYCLE)                            │
    │  ├── validateInput()      → 不正な引数を早期に拒否     │
    │  ├── checkPermissions()   → ツール固有の権限チェック   │
    │  └── call()               → 実行して結果を返す         │
    │                                                        │
    │  機能 (CAPABILITIES)                                   │
    │  ├── isEnabled()          → 機能フラグの確認           │
    │  ├── isConcurrencySafe()  → 並列実行可能か？           │
    │  ├── isReadOnly()         → 副作用がないか？           │
    │  ├── isDestructive()      → 元に戻せない操作か？       │
    │  └── interruptBehavior()  → キャンセルまたはユーザー待機？ │
    │                                                        │
    │  レンダリング (RENDERING - React/Ink)                  │
    │  ├── renderToolUseMessage()     → 入力表示             │
    │  ├── renderToolResultMessage()  → 出力表示             │
    │  ├── renderToolUseProgressMessage() → スピナー/状態表示 │
    │  └── renderGroupedToolUse()     → 並列ツールグループ表示 │
    │                                                        │
    │  AI 連携 (AI FACING)                                   │
    │  ├── prompt()             → LLM 向けツール説明         │
    │  ├── description()        → 動的な説明                 │
    │  └── mapToolResultToAPI() → API 応答用フォーマット     │
    └────────────────────────────────────────────────────────┘
```

### 完全なツールインベントリ

```text
    ファイル操作              検索と検出                 実行
    ═════════════════        ══════════════════════     ══════════
    FileReadTool             GlobTool                  BashTool
    FileEditTool             GrepTool                  PowerShellTool
    FileWriteTool            ToolSearchTool
    NotebookEditTool                                   対話
                                                       ═══════════
    Web とネットワーク        エージェント / タスク     AskUserQuestionTool
    ════════════════        ══════════════════        BriefTool
    WebFetchTool             AgentTool
    WebSearchTool            SendMessageTool           計画とワークフロー
                             TeamCreateTool            ════════════════════
    MCP プロトコル           TeamDeleteTool            EnterPlanModeTool
    ══════════════           TaskCreateTool            ExitPlanModeTool
    MCPTool                  TaskGetTool               EnterWorktreeTool
    ListMcpResourcesTool     TaskUpdateTool            ExitWorktreeTool
    ReadMcpResourceTool      TaskListTool              TodoWriteTool
                             TaskStopTool
                             TaskOutputTool            システム
                                                       ════════
                             スキルと拡張機能          ConfigTool
                             ═════════════════════     SkillTool
                             SkillTool                 ScheduleCronTool
                             LSPTool                   SleepTool
                                                       TungstenTool
```

---

## 権限システム

```text
    ツール呼び出しリクエスト
          │
          ▼
    ┌─ validateInput() ──────────────────────────────────┐
    │  権限チェックの前に無効な入力を早期に拒否          │
    └────────────────────┬───────────────────────────────┘
                         │
                         ▼
    ┌─ PreToolUse Hooks (ツール使用前フック) ────────────┐
    │  ユーザー定義のシェルコマンド (settings.json hooks)│
    │  可能な操作: 承認、拒否、または入力の変更          │
    └────────────────────┬───────────────────────────────┘
                         │
                         ▼
    ┌─ Permission Rules (権限ルール) ────────────────────┐
    │  alwaysAllowRules:  ツール名/パターン一致 → 自動承認 │
    │  alwaysDenyRules:   ツール名/パターン一致 → 自動拒否 │
    │  alwaysAskRules:    ツール名/パターン一致 → 常に確認 │
    │  ソース: 設定、CLI 引数、セッション内の決定        │
    └────────────────────┬───────────────────────────────┘
                         │
                    一致するルールなし？
                         │
                         ▼
    ┌─ Interactive Prompt (対話型プロンプト) ────────────┐
    │  ユーザーがツール名 + 入力値を確認                 │
    │  オプション: 1回許可 / 常に許可 / 拒否             │
    └────────────────────┬───────────────────────────────┘
                         │
                         ▼
    ┌─ checkPermissions() ───────────────────────────────┐
    │  ツール固有のロジック (例: パスサンドボックスの確認) │
    └────────────────────┬───────────────────────────────┘
                         │
                    承認済み → tool.call()
```

---

## サブエージェントとマルチエージェントアーキテクチャ

```text
                        メインエージェント
                        ==========
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
     ┌──────────────┐ ┌──────────┐ ┌──────────────┐
     │ フォークエージェント │ リモートエージェント │ プロセス内チームメイト│
     │ (FORK)       │ │ (REMOTE)   │ │ (IN-PROCESS)   │
     │ プロセスフォーク │ ブリッジセッション │ 同一プロセス   │
     │ キャッシュ共有 │ 完全隔離   │ 非同期コンテキスト │
     │ 新規 msgs[]  │ │            │ 状態共有         │
     └──────────────┘ └──────────┘ └──────────────┘

    生成モード (SPAWN MODES):
    ├─ default    → プロセス内、会話を共有
    ├─ fork       → 子プロセス、新しい messages[]、ファイルキャッシュを共有
    ├─ worktree   → 隔離された git worktree + fork
    └─ remote     → Claude Code Remote / コンテナへのブリッジ接続

    通信メカニズム (COMMUNICATION):
    ├─ SendMessageTool     → エージェント間のメッセージ伝達
    ├─ TaskCreate/Update   → 共有タスクボード
    └─ TeamCreate/Delete   → チームのライフサイクル管理

    スウォームモード (SWARM MODE、機能フラグで制御):
    ┌─────────────────────────────────────────────┐
    │  リーダーエージェント (Lead Agent)          │
    │    ├── チームメイト A ──> タスク 1 を担当   │
    │    ├── チームメイト B ──> タスク 2 を担当   │
    │    └── チームメイト C ──> タスク 3 を担当   │
    │                                             │
    │  共有: タスクボード、メッセージ受信トレイ   │
    │  隔離: messages[]、ファイルキャッシュ、cwd  │
    └─────────────────────────────────────────────┘
```

---

## コンテキスト管理 (圧縮システム)

```text
    コンテキストウィンドウ予算 (CONTEXT WINDOW BUDGET)
    ══════════════════════════════════════

    ┌─────────────────────────────────────────────────────┐
    │  システムプロンプト (ツール、権限、CLAUDE.md)       │
    │  ══════════════════════════════════════════════      │
    │                                                     │
    │  会話履歴 (Conversation History)                    │
    │  ┌─────────────────────────────────────────────┐    │
    │  │ [過去のメッセージの圧縮要約]                 │    │
    │  │ ═══════════════════════════════════════════  │    │
    │  │ [compact_boundary マーカー]                  │    │
    │  │ ─────────────────────────────────────────── │    │
    │  │ [最近のメッセージ — 元のまま保持]            │    │
    │  │ user → assistant → tool_use → tool_result   │    │
    │  └─────────────────────────────────────────────┘    │
    │                                                     │
    │  現在のターン (ユーザー + アシスタントの応答)       │
    └─────────────────────────────────────────────────────┘

    3つの圧縮戦略:
    ├─ autoCompact     → トークン数がしきい値を超えた時にトリガー
    │                     圧縮 API 呼び出しを通じて過去のメッセージを要約
    ├─ snipCompact     → 不要なメッセージと古いマーカーを削除
    │                     (HISTORY_SNIP 機能フラグ)
    └─ contextCollapse → 効率化のためにコンテキストを再構築
                         (CONTEXT_COLLAPSE 機能フラグ)

    圧縮フロー (COMPACTION FLOW):
    messages[] ──> getMessagesAfterCompactBoundary()
                        │
                        ▼
                  過去のメッセージ ──> Claude API (要約) ──> 圧縮要約
                        │
                        ▼
                  [要約] + [compact_boundary] + [最近のメッセージ]
```

---

## MCP (Model Context Protocol) 統合

```text
    ┌─────────────────────────────────────────────────────────┐
    │                  MCP アーキテクチャ                      │
    │                                                         │
    │  MCPConnectionManager.tsx                               │
    │    ├── サーバー検出 (settings.json の設定に基づく)      │
    │    │     ├── stdio  → 子プロセスを生成                  │
    │    │     ├── sse    → HTTP EventSource                  │
    │    │     ├── http   → ストリーミング HTTP               │
    │    │     ├── ws     → WebSocket                         │
    │    │     └── sdk    → プロセス内転送                    │
    │    │                                                    │
    │    ├── クライアントライフサイクル                       │
    │    │     ├── connect → initialize → list tools          │
    │    │     ├── MCPTool ラッパーを通じたツール呼び出し     │
    │    │     └── バックオフ (backoff) 付きの切断 / 再接続   │
    │    │                                                    │
    │    ├── 認証 (Authentication)                            │
    │    │     ├── OAuth 2.0 フロー (McpOAuthConfig)          │
    │    │     ├── クロスアプリアクセス (XAA / SEP-990)       │
    │    │     └── ヘッダーを通じた API キーの受け渡し        │
    │    │                                                    │
    │    └── ツール登録 (Tool Registration)                   │
    │          ├── mcp__<server>__<tool> 命名規則             │
    │          ├── MCP サーバーからの動的スキーマ (schema) 受信 │
    │          ├── Claude Code への権限パススルー (passthrough) │
    │          └── リソースのリスト化 (ListMcpResourcesTool)  │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
```

---

## ブリッジレイヤー (Claude Desktop / Remote)

```text
    Claude Desktop / Web / Cowork          Claude Code CLI
    ══════════════════════════            ══════════════

# FILE: README_KR.md

# Claude Code 아키텍처 학습 및 연구

> **소개**: 이 프로젝트는 CLI Agent 아키텍처에 대한 학습 및 연구 저장소입니다. 모든 자료는 전적으로 인터넷에 공개된 정보와 토론을 바탕으로 정리되었으며, 특히 현재 매우 인기 있는 CLI Agent인 `claude-code`와 관련된 공개 정보를 참고했습니다. 저희의 목적은 개발자들이 Agent 기술을 더 잘 이해하고 활용할 수 있도록 돕는 것입니다. 앞으로도 Agent 아키텍처와 관련된 더 많은 통찰과 실용적인 토론 콘텐츠를 지속적으로 공유할 예정입니다. 여러분의 관심과 성원에 감사드립니다!

> **면책 조항**: 본 저장소의 콘텐츠는 기술 연구, 학습, 교육 목적의 교류를 위해서만 제공됩니다. **상업적 사용은 엄격히 금지됩니다.** 어떠한 개인, 기관, 단체도 이 콘텐츠를 상업적 목적, 영리 활동, 불법 활동 또는 기타 무단 사용에 활용할 수 없습니다. 본 콘텐츠가 귀하의 법적 권리, 지적 재산권 또는 기타 이익을 침해하는 경우, 연락 주시면 즉시 확인 후 삭제 조치하겠습니다.


**언어**: [English](README.md) | [中文](README_CN.md) | **한국어** | [日本語](README_JA.md)

---

## 도구 시스템 및 권한 아키텍처

```text
                    도구 인터페이스
                    ==============

    buildTool(definition) ──> Tool<Input, Output, Progress>

    모든 도구는 다음을 구현합니다:
    ┌────────────────────────────────────────────────────────┐
    │  수명주기 (LIFECYCLE)                                  │
    │  ├── validateInput()      → 잘못된 인수 조기 거부      │
    │  ├── checkPermissions()   → 도구별 권한 검사           │
    │  └── call()               → 실행 및 결과 반환          │
    │                                                        │
    │  기능 (CAPABILITIES)                                   │
    │  ├── isEnabled()          → 기능 플래그 확인           │
    │  ├── isConcurrencySafe()  → 병렬 실행 가능 여부?       │
    │  ├── isReadOnly()         → 부작용(side effects) 없음? │
    │  ├── isDestructive()      → 되돌릴 수 없는 작업?       │
    │  └── interruptBehavior()  → 취소 또는 사용자 대기?     │
    │                                                        │
    │  렌더링 (RENDERING - React/Ink)                        │
    │  ├── renderToolUseMessage()     → 입력 표시            │
    │  ├── renderToolResultMessage()  → 출력 표시            │
    │  ├── renderToolUseProgressMessage() → 스피너/상태 표시 │
    │  └── renderGroupedToolUse()     → 병렬 도구 그룹 표시  │
    │                                                        │
    │  AI 연동 (AI FACING)                                   │
    │  ├── prompt()             → LLM용 도구 설명            │
    │  ├── description()        → 동적 설명                  │
    │  └── mapToolResultToAPI() → API 응답용 포맷팅          │
    └────────────────────────────────────────────────────────┘
```

### 전체 도구 인벤토리

```text
    파일 작업                 검색 및 탐색               실행
    ═════════════════        ══════════════════════     ══════════
    FileReadTool             GlobTool                  BashTool
    FileEditTool             GrepTool                  PowerShellTool
    FileWriteTool            ToolSearchTool
    NotebookEditTool                                   상호작용
                                                       ═══════════
    웹 및 네트워크           에이전트 / 작업           AskUserQuestionTool
    ════════════════        ══════════════════        BriefTool
    WebFetchTool             AgentTool
    WebSearchTool            SendMessageTool           계획 및 워크플로우
                             TeamCreateTool            ════════════════════
    MCP 프로토콜             TeamDeleteTool            EnterPlanModeTool
    ══════════════           TaskCreateTool            ExitPlanModeTool
    MCPTool                  TaskGetTool               EnterWorktreeTool
    ListMcpResourcesTool     TaskUpdateTool            ExitWorktreeTool
    ReadMcpResourceTool      TaskListTool              TodoWriteTool
                             TaskStopTool
                             TaskOutputTool            시스템
                                                       ════════
                             스킬 및 확장              ConfigTool
                             ═════════════════════     SkillTool
                             SkillTool                 ScheduleCronTool
                             LSPTool                   SleepTool
                                                       TungstenTool
```

---

## 권한 시스템

```text
    도구 호출 요청
          │
          ▼
    ┌─ validateInput() ──────────────────────────────────┐
    │  권한 검사 전 유효하지 않은 입력 조기 거부         │
    └────────────────────┬───────────────────────────────┘
                         │
                         ▼
    ┌─ PreToolUse Hooks (도구 사용 전 훅) ───────────────┐
    │  사용자 정의 쉘 명령 (settings.json hooks)         │
    │  가능 작업: 승인, 거부 또는 입력 수정              │
    └────────────────────┬───────────────────────────────┘
                         │
                         ▼
    ┌─ Permission Rules (권한 규칙) ─────────────────────┐
    │  alwaysAllowRules:  도구 이름/패턴 일치 → 자동 승인│
    │  alwaysDenyRules:   도구 이름/패턴 일치 → 자동 거부│
    │  alwaysAskRules:    도구 이름/패턴 일치 → 항상 확인│
    │  출처: 설정, CLI 인수, 세션 내 결정                │
    └────────────────────┬───────────────────────────────┘
                         │
                    일치하는 규칙 없음?
                         │
                         ▼
    ┌─ Interactive Prompt (대화형 프롬프트) ─────────────┐
    │  사용자가 도구 이름 + 입력값 확인                  │
    │  옵션: 한 번 허용 / 항상 허용 / 거부               │
    └────────────────────┬───────────────────────────────┘
                         │
                         ▼
    ┌─ checkPermissions() ───────────────────────────────┐
    │  도구별 특수 로직 (예: 경로 샌드박스 검사)         │
    └────────────────────┬───────────────────────────────┘
                         │
                    승인됨 → tool.call()
```

---

## 서브 에이전트 및 다중 에이전트 아키텍처

```text
                        메인 에이전트
                        ==========
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
     ┌──────────────┐ ┌──────────┐ ┌──────────────┐
     │ 포크 에이전트│ │ 원격 에이전트│ │ 프로세스 내 동료│
     │ (FORK)       │ │ (REMOTE)   │ │ (IN-PROCESS)   │
     │ 프로세스 포크│ │ 브릿지 세션│ │ 동일 프로세스  │
     │ 캐시 공유    │ │ 완전 격리  │ │ 비동기 컨텍스트│
     │ 새 msgs[]    │ │            │ │ 상태 공유      │
     └──────────────┘ └──────────┘ └──────────────┘

    생성 모드 (SPAWN MODES):
    ├─ default    → 프로세스 내, 대화 공유
    ├─ fork       → 자식 프로세스, 새로운 messages[], 파일 캐시 공유
    ├─ worktree   → 격리된 git worktree + fork
    └─ remote     → Claude Code Remote / 컨테이너로의 브릿지 연결

    통신 메커니즘 (COMMUNICATION):
    ├─ SendMessageTool     → 에이전트 간 메시지 전달
    ├─ TaskCreate/Update   → 공유 작업 보드(task board)
    └─ TeamCreate/Delete   → 팀 수명주기 관리

    스웜 모드 (SWARM MODE, 기능 플래그로 제어됨):
    ┌─────────────────────────────────────────────┐
    │  리더 에이전트 (Lead Agent)                 │
    │    ├── 동료 A ──> 작업 1 할당               │
    │    ├── 동료 B ──> 작업 2 할당               │
    │    └── 동료 C ──> 작업 3 할당               │
    │                                             │
    │  공유: 작업 보드, 메시지 수신함             │
    │  격리: messages[], 파일 캐시, cwd           │
    └─────────────────────────────────────────────┘
```

---

## 컨텍스트 관리 (압축 시스템)

```text
    컨텍스트 창 예산 (CONTEXT WINDOW BUDGET)
    ══════════════════════════════════════

    ┌─────────────────────────────────────────────────────┐
    │  시스템 프롬프트 (도구, 권한, CLAUDE.md)            │
    │  ══════════════════════════════════════════════      │
    │                                                     │
    │  대화 기록 (Conversation History)                   │
    │  ┌─────────────────────────────────────────────┐    │
    │  │ [이전 메시지들의 압축된 요약]                │    │
    │  │ ═══════════════════════════════════════════  │    │
    │  │ [compact_boundary 마커]                      │    │
    │  │ ─────────────────────────────────────────── │    │
    │  │ [최근 메시지 — 원본 그대로 유지]             │    │
    │  │ user → assistant → tool_use → tool_result   │    │
    │  └─────────────────────────────────────────────┘    │
    │                                                     │
    │  현재 턴 (사용자 + 어시스턴트 응답)                 │
    └─────────────────────────────────────────────────────┘

    3가지 압축 전략:
    ├─ autoCompact     → 토큰 수가 임계값을 초과할 때 트리거됨
    │                     압축 API 호출을 통해 이전 메시지 요약
    ├─ snipCompact     → 불필요한 메시지와 오래된 마커 제거
    │                     (HISTORY_SNIP 기능 플래그)
    └─ contextCollapse → 효율성을 위해 컨텍스트 재구성
                         (CONTEXT_COLLAPSE 기능 플래그)

    압축 흐름 (COMPACTION FLOW):
    messages[] ──> getMessagesAfterCompactBoundary()
                        │
                        ▼
                  이전 메시지 ──> Claude API (요약) ──> 압축된 요약
                        │
                        ▼
                  [요약] + [compact_boundary] + [최근 메시지]
```

---

## MCP (Model Context Protocol) 통합

```text
    ┌─────────────────────────────────────────────────────────┐
    │                  MCP 아키텍처                            │
    │                                                         │
    │  MCPConnectionManager.tsx                               │
    │    ├── 서버 검색 (settings.json 구성 기반)              │
    │    │     ├── stdio  → 자식 프로세스 생성                │
    │    │     ├── sse    → HTTP EventSource                  │
    │    │     ├── http   → 스트리밍 HTTP                     │
    │    │     ├── ws     → WebSocket                         │
    │    │     └── sdk    → 프로세스 내 전송                  │
    │    │                                                    │
    │    ├── 클라이언트 수명주기                              │
    │    │     ├── connect → initialize → list tools          │
    │    │     ├── MCPTool 래퍼를 통한 도구 호출              │
    │    │     └── 백오프(backoff)가 포함된 연결 해제 / 재연결│
    │    │                                                    │
    │    ├── 인증 (Authentication)                            │
    │    │     ├── OAuth 2.0 흐름 (McpOAuthConfig)            │
    │    │     ├── 교차 앱 액세스 (XAA / SEP-990)             │
    │    │     └── 헤더를 통한 API 키 전달                    │
    │    │                                                    │
    │    └── 도구 등록 (Tool Registration)                    │
    │          ├── mcp__<server>__<tool> 명명 규칙            │
    │          ├── MCP 서버로부터 동적 스키마(schema) 수신    │
    │          ├── Claude Code로 권한 통과(passthrough)       │
    │          └── 리소스 목록화 (ListMcpResourcesTool)       │
    │                                                         │
    └─────────────────────────────

# FILE: README.md

# Claude Code Architecture Study

> **Introduction**: This project is a learning and research repository focused on CLI Agent architecture. All materials are compiled entirely from publicly available online references and discussions, with a particular focus on public information regarding the highly popular CLI Agent `claude-code`. Our intention is to help developers better understand and utilize Agent technologies. We will continue to share more insights and practical discussions on Agent architecture in the future. Thank you for your support!

> **Disclaimer**: All content in this repository is provided strictly for technical research, study, and educational exchange among enthusiasts. **Commercial use is strictly prohibited.** No individual, organization, or entity may use this content for commercial purposes, profit-making activities, illegal activities, or any other unauthorized scenarios. If any content infringes upon your legal rights, intellectual property, or other interests, please contact us and we will verify and remove it immediately.


**Language**: **English** | [中文](README_CN.md) | [한국어](README_KR.md) | [日本語](README_JA.md)

---

## Table of Contents

- [Deep Analysis Reports (`docs/`)](#deep-analysis-reports-docs) — Telemetry, codenames, undercover mode, remote control, future roadmap
- [Directory Reference](#directory-reference) — Code structure tree
- [Architecture Overview](#architecture-overview) — Entry → Query Engine → Tools/Services/State
- [Tool System & Permissions](#tool-system-architecture) — 40+ tools, permission flow, sub-agents
- [The 12 Progressive Harness Mechanisms](#the-12-progressive-harness-mechanisms) — How Claude Code layers production features on the agent loop

---

## Deep Analysis Reports (`docs/`)

Deep analysis reports compiled from publicly available online references and community discussions on Claude Code v2.1.88. Quadrilingual (EN/JA/KO/ZH).

```
docs/
├── en/                                        # English
│   ├── [01-telemetry-and-privacy.md]          # Telemetry & Privacy — what's collected, why you can't opt out
│   ├── [02-hidden-features-and-codenames.md]  # Codenames (Capybara/Tengu/Numbat), feature flags, internal vs external
│   ├── [03-undercover-mode.md]                # Undercover Mode — hiding AI authorship in open-source repos
│   ├── [04-remote-control-and-killswitches.md]# Remote Control — managed settings, killswitches, model overrides
│   └── [05-future-roadmap.md]                 # Future Roadmap — Numbat, KAIROS, voice mode, unreleased tools
│
├── ja/                                        # 日本語
│   ├── [01-テレメトリとプライバシー.md]          # テレメトリとプライバシー — 収集項目、無効化不可の理由
│   ├── [02-隠し機能とコードネーム.md]           # 隠し機能 — モデルコードネーム、feature flag、内部/外部ユーザーの違い
│   ├── [03-アンダーカバーモード.md]             # アンダーカバーモード — オープンソースでのAI著作隠匿
│   ├── [04-リモート制御とキルスイッチ.md]       # リモート制御 — 管理設定、キルスイッチ、モデルオーバーライド
│   └── [05-今後のロードマップ.md]               # 今後のロードマップ — Numbat、KAIROS、音声モード、未公開ツール
│
├── ko/                                        # 한국어
│   ├── [01-텔레메트리와-프라이버시.md]          # 텔레메트리 및 프라이버시 — 수집 항목, 비활성화 불가 이유
│   ├── [02-숨겨진-기능과-코드네임.md]          # 숨겨진 기능 — 모델 코드네임, feature flag, 내부/외부 사용자 차이
│   ├── [03-언더커버-모드.md]                   # 언더커버 모드 — 오픈소스에서 AI 저작 은폐
│   ├── [04-원격-제어와-킬스위치.md]            # 원격 제어 — 관리 설정, 킬스위치, 모델 오버라이드
│   └── [05-향후-로드맵.md]                     # 향후 로드맵 — Numbat, KAIROS, 음성 모드, 미공개 도구
│
└── zh/                                        # 中文
    ├── [01-遥测与隐私分析.md]                    # 遥测与隐私 — 收集了什么，为什么无法退出
    ├── [02-隐藏功能与模型代号.md]                # 隐藏功能 — 模型代号，feature flag，内外用户差异
    ├── [03-卧底模式分析.md]                     # 卧底模式 — 在开源项目中隐藏 AI 身份
    ├── [04-远程控制与紧急开关.md]                # 远程控制 — 托管设置，紧急开关，模型覆盖
    └── [05-未来路线图.md]                       # 未来路线图 — Numbat，KAIROS，语音模式，未上线工具
```

> Click any filename above to jump to the full report.

| # | Topic | Key Findings |
|---|-------|-------------|
| 01 | **Telemetry & Privacy** | Two analytics sinks (1P, Datadog). Environment fingerprint, process metrics, repo hash on every event. **No UI-exposed opt-out** for 1st-party logging. `OTEL_LOG_TOOL_DETAILS=1` enables full tool input capture. |
| 02 | **Hidden Features & Codenames** | Animal codenames (Capybara v8, Tengu, Fennec→Opus 4.6, **Numbat** next). Feature flags use random word pairs (`tengu_frond_boric`) to obscure purpose. Internal users get better prompts, verification agents, and effort anchors. Hidden commands: `/btw`, `/stickers`. |
| 03 | **Undercover Mode** | Official employees auto-enter undercover mode in public repos. Model instructed: *"Do not blow your cover"* — strip all AI attribution, write commits "as a human developer would." **No force-OFF exists.** Raises transparency questions for open-source communities. |
| 04 | **Remote Control** | Hourly polling of `/api/claude_code/settings`. Dangerous changes show blocking dialog — **reject = app exits**. 6+ killswitches (bypass permissions, fast mode, voice mode, analytics sink). GrowthBook flags can change any user's behavior without consent. |
| 05 | **Future Roadmap** | **Numbat** codename confirmed. Opus 4.7 / Sonnet 4.8 in development. **KAIROS** = fully autonomous agent mode with `<tick>` heartbeats, push notifications, PR subscriptions. Voice mode (push-to-talk) ready but gated. 17 unreleased tools found. |

---

## Copyright & Disclaimer

```text
This repository is provided strictly for technical research and educational purposes.
Commercial use is strictly prohibited.

If you are the copyright owner and believe this repository content infringes your rights,
please contact the repository owner for immediate removal.
```

---

## Stats

| Item | Count |
|------|-------|
| Files (.ts/.tsx) | ~1,884 |
| Lines | ~512,664 |
| Largest single file | `query.ts` (~785KB) |
| Built-in tools | ~40+ |
| Slash commands | ~80+ |
| Dependencies (node_modules) | ~192 packages |
| Runtime | Bun (compiled to Node.js >= 18 bundle) |

---

## The Agent Pattern

```
                    THE CORE LOOP
                    =============

    User --> messages[] --> Claude API --> response
                                          |
                                stop_reason == "tool_use"?
                               /                          \
                             yes                           no
                              |                             |
                        execute tools                    return text
                        append tool_result
                        loop back -----------------> messages[]


    That is the minimal agent loop. Claude Code wraps this loop
    with a production-grade harness: permissions, streaming,
    concurrency, compaction, sub-agents, persistence, and MCP.
```

---

## Directory Reference

```
src/
├── main.tsx                 # REPL bootstrap, 4,683 lines
├── QueryEngine.ts           # SDK/headless query lifecycle engine
├── query.ts                 # Main agent loop (785KB, largest file)
├── Tool.ts                  # Tool interface + buildTool factory
├── Task.ts                  # Task types, IDs, state base
├── tools.ts                 # Tool registry, presets, filtering
├── commands.ts              # Slash command definitions
├── context.ts               # User input context
├── cost-tracker.ts          # API cost accumulation
├── setup.ts                 # First-run setup flow
│
├── bridge/                  # Claude Desktop / remote bridge
│   ├── bridgeMain.ts        #   Session lifecycle manager
│   ├── bridgeApi.ts         #   HTTP client
│   ├── bridgeConfig.ts      #   Connection config
│   ├── bridgeMessaging.ts   #   Message relay
│   ├── sessionRunner.ts     #   Process spawning
│   ├── jwtUtils.ts          #   JWT refresh
│   ├── workSecret.ts        #   Auth tokens
│   └── capacityWake.ts      #   Capacity-based wakeup
│
├── cli/                     # CLI infrastructure
│   ├── handlers/            #   Command handlers
│   └── transports/          #   I/O transports (stdio, structured)
│
├── commands/                # ~80 slash commands
│   ├── agents/              #   Agent management
│   ├── compact/             #   Context compaction
│   ├── config/              #   Settings management
│   ├── help/                #   Help display
│   ├── login/               #   Authentication
│   ├── mcp/                 #   MCP server management
│   ├── memory/              #   Memory system
│   ├── plan/                #   Plan mode
│   ├── resume/              #   Session resume
│   ├── review/              #   Code review
│   └── ...                  #   70+ more commands
│
├── components/              # React/Ink terminal UI
│   ├── design-system/       #   Reusable UI primitives
│   ├── messages/            #   Message rendering
│   ├── permissions/         #   Permission dialogs
│   ├── PromptInput/         #   Input field + suggestions
│   ├── LogoV2/              #   Branding + welcome screen
│   ├── Settings/            #   Settings panels
│   ├── Spinner.tsx          #   Loading indicators
│   └── ...                  #   40+ component groups
│
├── entrypoints/             # Application entry points
│   ├── cli.tsx              #   CLI main (version, help, daemon)
│   ├── sdk/                 #   Agent SDK (types, sessions)
│   └── mcp.ts               #   MCP server entry
│
├── hooks/                   # React hooks
│   ├── useCanUseTool.tsx    #   Permission checking
│   ├── useReplBridge.tsx    #   Bridge connection
│   ├── notifs/              #   Notification hooks
│   └── toolPermission/      #   Tool permission handlers
│
├── services/                # Business logic layer
│   ├── api/                 #   Claude API client
│   │   ├── claude.ts        #     Streaming API calls
│   │   ├── errors.ts        #     Error categorization
│   │   └── withRetry.ts     #     Retry logic
│   ├── analytics/           #   Telemetry + GrowthBook
│   ├── compact/             #   Context compression
│   

# FILE: docs/ja/05-今後のロードマップ.md

# 今後のロードマップ — アーキテクチャが示すもの

> インターネット上で公開されている資料やコミュニティの議論をもとに整理した Claude Code v2.1.88 分析レポート。

## 1. 次期モデル: Numbat

次期モデルリリースの最も具体的な根拠:

```typescript
// src/constants/prompts.ts:402
// @[MODEL LAUNCH]: Remove this section when we launch numbat.
```

**Numbat**（ナンバット）は次期モデルのコードネームである。このコメントはNumbatリリース時に出力効率セクションが改訂されることを示しており、より優れたネイティブ出力制御を備える可能性を示唆している。

### 今後のバージョン番号

```typescript
// src/utils/undercover.ts:49
- Unreleased model version numbers (e.g., opus-4-7, sonnet-4-8)
```

**Opus 4.7** と **Sonnet 4.8** が開発中である。

### コードネームの変遷

```
Fennec（フェネック） → Opus 4.6 → [Numbat?]
Capybara（カピバラ） → Sonnet v8 → [?]
Tengu（天狗） → テレメトリ/製品接頭辞
```

FennecからOpusへのマイグレーションが文書化されている:

```typescript
// src/migrations/migrateFennecToOpus.ts:7-11
// fennec-latest → opus
// fennec-latest[1m] → opus[1m]
// fennec-fast-latest → opus[1m] + fast mode
```

### MODEL LAUNCHチェックリスト

コードベースには更新項目を列挙した20以上の `@[MODEL LAUNCH]` マーカーがある:

- デフォルトモデル名（`FRONTIER_MODEL_NAME`）
- モデルファミリーID
- ナレッジカットオフ日
- 料金表
- コンテキストウィンドウ設定
- Thinkingモードサポートフラグ
- 表示名マッピング
- マイグレーションスクリプト

## 2. KAIROS — 自律エージェントモード

最大規模の未公開機能であり、KAIROSはClaude Codeを受動的アシスタントから能動的自律エージェントに変換する。

### システムプロンプト（抜粋）

```
// src/constants/prompts.ts:860-913

You are running autonomously.
You will receive <tick> prompts that keep you alive between turns.
If you have nothing useful to do, call SleepTool.
Bias toward action — read files, make changes, commit without asking.

## Terminal focus
- Unfocused: The user is away. Lean heavily into autonomous action.
- Focused: The user is watching. Be more collaborative.
```

### 関連ツール

| ツール | Feature Flag | 用途 |
|-------|-------------|------|
| SleepTool | KAIROS / PROACTIVE | 自律動作間のペーシング制御 |
| SendUserFileTool | KAIROS | ユーザーへのファイル先行送信 |
| PushNotificationTool | KAIROS / KAIROS_PUSH_NOTIFICATION | ユーザーデバイスへのプッシュ通知 |
| SubscribePRTool | KAIROS_GITHUB_WEBHOOKS | GitHub PRウェブフック購読 |
| BriefTool | KAIROS_BRIEF | 先行ステータス更新 |

### 動作方式

- `<tick>` ハートビートプロンプトで稼働
- ターミナルフォーカス状態に応じて自律レベルを調整
- 独立してコミット、プッシュ、意思決定が可能
- 先行的に通知とステータス更新を送信
- GitHub PRの変更を監視

## 3. 音声モード

Push-to-talk音声入力が完全実装されているが `VOICE_MODE` feature flagでゲートされている。

```typescript
// src/voice/voiceModeEnabled.ts
// Anthropicのvoice_stream WebSocketエンドポイントに接続
// conversation_engineベースのモデルで音声テキスト変換
// キーバインドを長押しで録音、離すと送信
```

- OAuth専用（APIキー / Bedrock / Vertex非対応）
- WebSocket接続にmTLSを使用
- キルスイッチ: `tengu_amber_quartz_disabled`

## 4. 未公開ツール

アーキテクチャに存在するが外部ユーザーにはまだ有効化されていないツール:

| ツール | Feature Flag | 説明 |
|-------|-------------|------|
| **WebBrowserTool** | `WEB_BROWSER_TOOL` | 内蔵ブラウザ自動化（コードネーム: bagel） |
| **TerminalCaptureTool** | `TERMINAL_PANEL` | ターミナルパネルキャプチャと監視 |
| **WorkflowTool** | `WORKFLOW_SCRIPTS` | 定義済みワークフロースクリプト実行 |
| **MonitorTool** | `MONITOR_TOOL` | システム/プロセス監視 |
| **SnipTool** | `HISTORY_SNIP` | 会話履歴のスニッピング/縮小 |
| **ListPeersTool** | `UDS_INBOX` | Unixドメインソケットピア探索 |
| **RemoteTriggerTool** | `AGENT_TRIGGERS_REMOTE` | リモートエージェントトリガー |
| **TungstenTool** | ant専用 | 内部パフォーマンス監視パネル |
| **VerifyPlanExecutionTool** | VERIFY_PLAN env | 計画実行検証 |
| **OverflowTestTool** | `OVERFLOW_TEST_TOOL` | コンテキストオーバーフローテスト |
| **SubscribePRTool** | `KAIROS_GITHUB_WEBHOOKS` | GitHub PRウェブフック購読 |

## 5. Coordinatorモード

マルチエージェント連携システム:

```typescript
// src/coordinator/coordinatorMode.ts
// Feature flag: COORDINATOR_MODE
```

共有状態とメッセージングによる複数エージェント間の連携タスク実行を実現する。

## 6. Buddyシステム（バーチャルペット）

完全なペットコンパニオンシステムが実装されているが未リリース:

- **18種**: duck, goose, blob, cat, dragon, octopus, owl, penguin, turtle, snail, ghost, axolotl, capybara, cactus, robot, rabbit, mushroom, chonk
- **5段階レアリティ**: Common (60%), Uncommon (25%), Rare (10%), Epic (4%), Legendary (1%)
- **7種の帽子**: crown, tophat, propeller, halo, wizard, beanie, tinyduck
- **5つのステータス**: DEBUGGING, PATIENCE, CHAOS, WISDOM, SNARK
- **1%のシャイニー確率**: 全種のSparkleバリアント
- **決定論的生成**: ユーザーIDハッシュに基づく

出典: `src/buddy/`

## 7. Dream Task

バックグラウンド記憶統合サブエージェント:

```
// src/tasks/DreamTask/
// バックグラウンドで動作するオートドリーミング機能
// 'tengu_onyx_plover' feature flagで制御
```

アイドル時間中にAIが自律的に記憶を処理・統合できるようにする。

## まとめ: 3つの方向性

1. **新モデル**: Numbat（次期）、Opus 4.7、Sonnet 4.8が開発中
2. **自律エージェント**: KAIROSモード — 無人運用、先行アクション、プッシュ通知
3. **マルチモーダル**: 音声入力準備完了、ブラウザツール待機中、ワークフロー自動化予定

Claude Codeは**コーディングアシスタント**から**常時稼働の自律開発エージェント**へと進化している。


# FILE: docs/ja/02-隠し機能とコードネーム.md

# 隠し機能とモデルコードネーム

> インターネット上で公開されている資料やコミュニティの議論をもとに整理した Claude Code v2.1.88 分析レポート。

## モデルコードネーム体系

Anthropicは内部モデルコードネームに**動物名**を使用している。外部ビルドへの漏洩を積極的に防止している。

### 既知のコードネーム

| コードネーム | 役割 | 根拠 |
|-------------|------|------|
| **Tengu**（天狗） | 製品/テレメトリ接頭辞、モデルの可能性あり | 250以上の分析イベントとfeature flagに `tengu_*` 接頭辞で使用 |
| **Capybara**（カピバラ） | Sonnet系モデル、現在v8 | `capybara-v2-fast[1m]`、v8動作問題のパッチあり |
| **Fennec**（フェネック） | Opus 4.6の前身モデル | マイグレーション: `fennec-latest` → `opus` |
| **Numbat**（ナンバット） | 次期モデル | コメント: "Remove this section when we launch numbat" |

### コードネーム保護

`undercover` モードで保護対象コードネームが明示されている:

```typescript
// src/utils/undercover.ts:48-49
NEVER include in commit messages or PR descriptions:
- Internal model codenames (animal names like Capybara, Tengu, etc.)
- Unreleased model version numbers (e.g., opus-4-7, sonnet-4-8)
```

ビルドシステムは `scripts/excluded-strings.txt` を使用してコードネームの漏洩を検出する。Buddyシステムの種（species）は `String.fromCharCode()` でエンコードし、カナリア検出を回避している:

```typescript
// src/buddy/types.ts:10-13
// One species name collides with a model-codename canary in excluded-strings.txt.
// The check greps build output (not source), so runtime-constructing the value keeps
// the literal out of the bundle while the check stays armed for the actual codename.
```

衝突する種は **capybara** — ペットの種でありモデルコードネームでもある。

### Capybara動作問題（v8）

アーキテクチャからCapybara v8の具体的な動作問題が確認される:

1. **Stop sequenceの誤発動**（プロンプト末尾に `<functions>` がある場合、約10%の発生率）
   - 出典: `src/utils/messages.ts:2141`

2. **空のtool_resultで出力ゼロ**
   - 出典: `src/utils/toolResultStorage.ts:281`

3. **コメント過剰挿入** — 専用コメント抑制プロンプトパッチが必要
   - 出典: `src/constants/prompts.ts:204`

4. **高い虚偽主張率**: v8は29-30%、v4は16.7%
   - 出典: `src/constants/prompts.ts:237`

5. **不十分な検証** — "徹底度カウンターウェイト（thoroughness counterweight）"が必要
   - 出典: `src/constants/prompts.ts:210`

## Feature Flag命名規則

すべてのfeature flagは `tengu_` 接頭辞に**ランダムな単語ペア**を使用し、目的を難読化している:

| Flag | 用途 |
|------|------|
| `tengu_onyx_plover` | Auto Dream（バックグラウンド記憶統合） |
| `tengu_coral_fern` | memdir機能 |
| `tengu_moth_copse` | memdir追加スイッチ |
| `tengu_herring_clock` | Team memory |
| `tengu_passport_quail` | Path機能 |
| `tengu_slate_thimble` | memdir追加スイッチ |
| `tengu_sedge_lantern` | Away Summary |
| `tengu_frond_boric` | 分析キルスイッチ |
| `tengu_amber_quartz_disabled` | 音声モードキルスイッチ |
| `tengu_amber_flint` | Agent teams |
| `tengu_hive_evidence` | 検証エージェント |

ランダムな単語パターン（形容詞/素材 + 自然/物体）により、外部の観察者がflag名から機能の目的を推測することを防ぐ。

## 内部ユーザーと外部ユーザーの違い

Anthropic社員（`USER_TYPE === 'ant'`）は大幅に優遇されている:

### プロンプトの違い（`src/constants/prompts.ts`）

| 項目 | 外部ユーザー | 内部ユーザー（ant） |
|------|------------|-------------------|
| 出力スタイル | "Be extra concise"（極めて簡潔に） | "Err on the side of more explanation"（説明を多めに） |
| 虚偽主張対策 | なし | 専用Capybara v8パッチ適用 |
| 数値的長さ基準 | なし | "ツール間≤25単語、最終回答≤100単語" |
| 検証エージェント | なし | 非自明な変更に必須 |
| コメントガイド | 一般的 | 専用コメント過剰防止プロンプト |
| 先制的修正 | なし | "ユーザーに誤解があれば指摘する" |

### ツールアクセス

内部ユーザーのみアクセス可能なツール:
- `REPLTool` — REPLモード
- `SuggestBackgroundPRTool` — バックグラウンドPR提案
- `TungstenTool` — パフォーマンス監視パネル
- `VerifyPlanExecutionTool` — 計画実行検証
- Agent入れ子（エージェントがエージェントを生成）

## 隠しコマンド

| コマンド | 状態 | 説明 |
|---------|------|------|
| `/btw` | 有効 | 作業中断なしで余談質問 |
| `/stickers` | 有効 | Claude Codeステッカー注文（ブラウザが開く） |
| `/thinkback` | 有効 | 2025年振り返り |
| `/effort` | 有効 | モデル努力レベル設定 |
| `/good-claude` | スタブ | 隠しプレースホルダー |
| `/bughunter` | スタブ | 隠しプレースホルダー |


# FILE: docs/ja/04-リモート制御とキルスイッチ.md

# リモート制御およびキルスイッチ

> インターネット上で公開されている資料やコミュニティの議論をもとに整理した Claude Code v2.1.88 分析レポート。

## 概要

Claude Codeは、公式管理者（および企業管理者）がシステムセキュリティと企業のコンプライアンスを確保するために、リモート構成を通じて特定のクライアントの動作を管理および更新できるリモート管理メカニズムを実装しています。

## 1. リモート管理設定

### 構成

対象セッションは以下から設定を取得する:
```
GET /api/claude_code/settings
```

出典: `src/services/remoteManagedSettings/index.ts:105-107`

### ポーリング動作

```typescript
// src/services/remoteManagedSettings/index.ts:52-54
const SETTINGS_TIMEOUT_MS = 10000
const DEFAULT_MAX_RETRIES = 5
const POLLING_INTERVAL_MS = 60 * 60 * 1000 // 1時間
```

設定は1時間ごとにポーリングされ、失敗時は最大5回リトライする。

### 対象資格

- Consoleユーザー（APIキー）: 全員対象
- OAuthユーザー: Enterprise/C4EおよびTeamサブスクライバーのみ

### 強制承認ダイアログ

リモート設定に「危険な」変更が含まれる場合、ブロッキングダイアログが表示される:

```typescript
// src/services/remoteManagedSettings/securityCheck.tsx:67-73
export function handleSecurityCheckResult(result: SecurityCheckResult): boolean {
  if (result === 'rejected') {
    gracefulShutdownSync(1)  // 終了コード1で終了
    return false
  }
  return true
}
```

リモート設定を拒否するとアプリケーションが**強制終了される**。選択肢はリモート設定の承認またはClaude Codeの終了のみである。

### 障害時の動作

リモートサーバーに接続できない場合、ディスクキャッシュ設定が使用される:

```typescript
// src/services/remoteManagedSettings/index.ts:433-436
if (cachedSettings) {
  logForDebugging('Remote settings: Using stale cache after fetch failure')
  setSessionCache(cachedSettings)
  return cachedSettings
}
```

リモート設定が一度適用されると、サーバー障害時もキャッシュが維持される。

## 2. Feature Flagキルスイッチ

GrowthBook feature flagにより複数の機能をリモート無効化できる:

### パーミッションバイパスキルスイッチ

```typescript
// src/utils/permissions/bypassPermissionsKillswitch.ts
// Statsigゲートを確認してパーミッションバイパスを無効化
```

ユーザーの同意なくパーミッションバイパス機能を無効化できる。

### Autoモードサーキットブレーカー

```typescript
// src/utils/permissions/autoModeState.ts
// autoModeCircuitBroken状態でautoモードへの再突入を阻止
```

Autoモードをリモートで無効化できる。

### Fastモードキルスイッチ

```typescript
// src/utils/fastMode.ts
// /api/claude_code_penguin_mode から取得
// 特定ユーザーのfastモードを永久に無効化可能
```

### 分析シンクキルスイッチ

```typescript
// src/services/analytics/sinkKillswitch.ts:4
const SINK_KILLSWITCH_CONFIG_NAME = 'tengu_frond_boric'
```

すべての分析出力をリモートで停止できる。

### Agent Teamsキルスイッチ

```typescript
// src/utils/agentSwarmsEnabled.ts
// 環境変数とGrowthBookゲート 'tengu_amber_flint' の両方が必要
```

### 音声モードキルスイッチ

```typescript
// src/voice/voiceModeEnabled.ts:21
// 'tengu_amber_quartz_disabled' — 音声モードの緊急停止
```

## 3. モデルオーバーライドシステム

カナリアテストを実施したり、予期せぬオンラインの状況に対応するために、システムは内部社員などの特定のグループに対してモデルバージョンを動的に切り替えることをサポートしています:

```typescript
// src/utils/model/antModels.ts:32-33
// @[MODEL LAUNCH]: tengu_ant_model_overrideに新しいant専用モデルを更新
// @[MODEL LAUNCH]: コードネームをscripts/excluded-strings.txtに追加
```

`tengu_ant_model_override` GrowthBook flagで可能な操作:
- デフォルトモデルの設定
- デフォルト努力レベルの設定
- システムプロンプトへの内容追加
- カスタムモデルエイリアスの定義

## 4. Penguinモード

Fastモードの状態は専用エンドポイントから取得される:

```typescript
// src/utils/fastMode.ts
// GET /api/claude_code_penguin_mode
// APIが無効を返した場合、該当ユーザーで永久無効化
```

Fastモードの可用性を制御するfeature flag:
- `tengu_penguins_off`
- `tengu_marble_sandcastle`

## まとめ

| メカニズム | 対象範囲 | ユーザー同意 |
|-----------|---------|------------|
| リモート管理設定 | Enterprise/Team | 承認または終了 |
| GrowthBook feature flag | 全ユーザー | なし |
| キルスイッチ | 全ユーザー | なし |
| モデルオーバーライド | 内部（ant） | なし |
| Fastモード制御 | 全ユーザー | なし |

リモート制御インフラは広範にわたります。企業管理者はユーザーが上書きできないポリシーを強制することができ、システムは重大な問題に対処するために、機能フラグ（feature flags）を通じてすべてのユーザーの動作をリモートで変更できます。


# FILE: docs/ja/03-アンダーカバーモード.md

# アンダーカバーモード分析

> インターネット上で公開されている資料やコミュニティの議論をもとに整理した Claude Code v2.1.88 分析レポート。

## アンダーカバーモードとは

アンダーカバーモードは、公式社員が外部/オープンソースリポジトリで作業する際に使用する安全保護メカニズムです。有効化すると、内部固有の AI モデル情報や帰属表示が隠され、コミットされたコードが人間の開発者の貢献と同じように見えるようになります。これは主に、内部の機密情報や未公開モデルの名称がオープンソースコミュニティに漏洩するのを防ぐためのものです。

出典: `src/utils/undercover.ts`

## 有効化条件

```typescript
// src/utils/undercover.ts:28-37
export function isUndercover(): boolean {
  if (process.env.USER_TYPE === 'ant') {
    if (isEnvTruthy(process.env.CLAUDE_CODE_UNDERCOVER)) return true
    // Auto: 内部リポジトリと確認されない限り自動有効化
    return getRepoClassCached() !== 'internal'
  }
  return false
}
```

主な特性:
- **内部専用**: 公式社員（`USER_TYPE === 'ant'`）のみ対象
- **デフォルト有効**: 内部許可リストにないすべてのリポジトリで自動有効化
- **強制無効化不可**: "There is NO force-OFF. This guards against model codename leaks"
- **外部ビルド**: バンドラーによりデッドコード除去され、実行されない

## モデルに渡されるプロンプト

```typescript
// src/utils/undercover.ts:39-69
export function getUndercoverInstructions(): string {
  return `## UNDERCOVER MODE — CRITICAL

You are operating UNDERCOVER in a PUBLIC/OPEN-SOURCE repository. Your commit
messages, PR titles, and PR bodies MUST NOT contain ANY Anthropic-internal
information. Do not blow your cover.

NEVER include in commit messages or PR descriptions:
- Internal model codenames (animal names like Capybara, Tengu, etc.)
- Unreleased model version numbers (e.g., opus-4-7, sonnet-4-8)
- Internal repo or project names (e.g., claude-cli-internal, anthropics/…)
- Internal tooling, Slack channels, or short links (e.g., go/cc, #claude-code-…)
- The phrase "Claude Code" or any mention that you are an AI
- Any hint of what model or version you are
- Co-Authored-By lines or any other attribution

Write commit messages as a human developer would — describe only what the code
change does.

GOOD:
- "Fix race condition in file watcher initialization"
- "Add support for custom key bindings"

BAD (never write these):
- "Fix bug found while testing with Claude Capybara"
- "1-shotted by claude-opus-4-6"
- "Generated with Claude Code"
- "Co-Authored-By: Claude Opus 4.6 <…>"`
}
```

## 帰属表示システム

帰属表示システム（`src/utils/attribution.ts`、`src/utils/commitAttribution.ts`）はアンダーカバーモードを補完する:

```typescript
// src/utils/attribution.ts:70-72
// @[MODEL LAUNCH]: 以下のハードコードされたフォールバックモデル名を更新
// （コードネーム漏洩防止用）。
// 外部リポジトリでは、認識されないモデルは "Claude Opus 4.6" にフォールバック。
```

```typescript
// src/utils/model/model.ts:386-392
function maskModelCodename(baseName: string): string {
  // e.g. capybara-v2-fast → cap*****-v2-fast
  const [codename = '', ...rest] = baseName.split('-')
  const masked = codename.slice(0, 3) + '*'.repeat(Math.max(0, codename.length - 3))
  return [masked, ...rest].join('-')
}
```

## 示唆

### オープンソースへの影響

公式社員がClaude Codeでオープンソースプロジェクトにコントリビュートする場合:
1. AIがコードを書くが、コミットは人間が書いたものとして表示される
2. "Co-Authored-By: Claude"の帰属表示がない
3. "Generated with Claude Code"のマーカーがない
4. プロジェクトメンテナーやコミュニティはAI生成のコントリビュートを識別できない
5. AIコントリビュートに関するオープンソースの透明性規範に抵触する可能性がある

### 公式保護目的

主な目的は以下の偶発的漏洩の防止:
- 内部モデルコードネーム（競争情報）
- 未公開バージョン番号（市場タイミング）
- 内部インフラの詳細（セキュリティ）

### 倫理的考察

"Do not blow your cover（正体を明かすな）"という表現はAIを潜入工作員として位置づけている。公開コードコントリビュートにおけるAI著作の意図的な隠匿は以下の問題を提起する:
- オープンソースコミュニティにおける透明性
- プロジェクトコントリビュートガイドラインの遵守
- 営業秘密保護と欺瞞の境界線


# FILE: docs/ja/01-テレメトリとプライバシー.md

# テレメトリおよびプライバシー分析

> インターネット上で公開されている資料やコミュニティの議論をもとに整理した Claude Code v2.1.88 分析レポート。

## 概要

Claude Codeは二層の分析パイプラインを実装し、広範な環境情報と使用メタデータを収集している。キーロギングやユーザーコード流出の証拠はないが、収集範囲の広さと完全な無効化が不可能な点にプライバシー上の懸念がある。

## データパイプライン構成

### ファーストパーティロギング（1P）

- **エンドポイント**: `https://api.anthropic.com/api/event_logging/batch`
- **プロトコル**: OpenTelemetry + Protocol Buffers
- **バッチサイズ**: 最大200イベント、10秒間隔で送信
- **リトライ**: 二次バックオフ、最大8回、ディスク永続化
- **ストレージ**: 送信失敗時 `~/.claude/telemetry/` に保存

出典: `src/services/analytics/firstPartyEventLoggingExporter.ts`

### サードパーティロギング（Datadog）

- **エンドポイント**: `https://http-intake.logs.us5.datadoghq.com/api/v2/logs`
- **対象**: 事前承認済みの64種類のイベントに限定
- **トークン**: `pubbbf48e6d78dae54bceaa4acf463299bf`

出典: `src/services/analytics/datadog.ts`

## 収集項目

### 環境フィンガープリント

すべてのイベントに以下のメタデータが含まれる（`src/services/analytics/metadata.ts:417-452`）:

```
- platform, platformRaw, arch, nodeVersion
- ターミナル種別
- インストール済みパッケージマネージャとランタイム
- CI/CD検出、GitHub Actionsメタデータ
- WSLバージョン、Linuxディストリビューション、カーネルバージョン
- VCS（バージョン管理システム）種別
- Claude Codeバージョンとビルド日時
- デプロイ環境
```

### プロセスメトリクス（`metadata.ts:457-467`）

```
- uptime, rss, heapTotal, heapUsed
- CPU使用量と使用率
- memory arraysとexternal allocations
```

### ユーザー追跡（`metadata.ts:472-496`）

```
- 使用中のモデル
- セッションID、ユーザーID、デバイスID
- アカウントUUID、組織UUID
- サブスクリプション等級（max, pro, enterprise, team）
- リポジトリリモートURLハッシュ（SHA256、先頭16文字）
- エージェント種別、チーム名、親セッションID
```

### ツール入力ロギング

ツール入力はデフォルトで切り詰められる:

```
- 文字列: 512文字で切り詰め、128文字+省略記号で表示
- JSON: 4,096文字制限
- 配列: 最大20要素
- ネストオブジェクト: 最大2階層
```

出典: `metadata.ts:236-241`

ただし、`OTEL_LOG_TOOL_DETAILS=1` 設定時は**ツール入力がすべて記録される**。

出典: `metadata.ts:86-88`

### ファイル拡張子追跡

`rm, mv, cp, touch, mkdir, chmod, chown, cat, head, tail, sort, stat, diff, wc, grep, rg, sed` 関連のBashコマンドで、ファイル引数の拡張子が抽出・記録される。

出典: `metadata.ts:340-412`

## 無効化の問題

ファーストパーティロギングパイプラインは、直接Anthropic APIユーザーの場合**無効化できない**。

```typescript
// src/services/analytics/firstPartyEventLogger.ts:141-144
export function is1PEventLoggingEnabled(): boolean {
  return !isAnalyticsDisabled()
}
```

`isAnalyticsDisabled()` がtrueを返すケース:
- テスト環境
- サードパーティクラウドプロバイダ（Bedrock, Vertex）
- グローバルテレメトリ無効化（設定UIに非公開）

ファーストパーティイベントロギングを無効化する**ユーザー向け設定は存在しない**。

## GrowthBook A/Bテスト

ユーザーは明示的な同意なくGrowthBookを通じて実験グループに割り当てられる。送信されるユーザー属性:

```
- id, sessionId, deviceID
- platform, organizationUUID, subscriptionType
```

出典: `src/services/analytics/growthbook.ts`

## 要点

1. **収集量**: セッションあたり数百件のイベントが収集される
2. **無効化不可**: 直接APIユーザーはファーストパーティロギングを停止できない
3. **永続性**: 送信失敗イベントはディスクに保存され積極的にリトライされる
4. **サードパーティ共有**: データがDatadogに送信される
5. **ツール詳細バックドア**: `OTEL_LOG_TOOL_DETAILS=1` で全入力ロギングが有効化される
6. **リポジトリフィンガープリント**: リポジトリURLがハッシュ化されサーバー側の相関分析に使用される


# FILE: docs/zh/04-远程控制与紧急开关.md

# 远程控制与紧急开关

> 基于网络公开资料与社区讨论整理的 Claude Code v2.1.88 分析报告。

## 概述

Claude Code 实现了远程管理机制，允许官方（和企业管理员）通过远程配置来管理和更新客户端的特定行为，以确保系统安全和企业合规。

## 1. 远程托管设置

### 架构

客户端会从以下端点获取最新的配置信息：
```
GET /api/claude_code/settings
```

来源: `src/services/remoteManagedSettings/index.ts`

### 轮询行为

```typescript
const POLLING_INTERVAL_MS = 60 * 60 * 1000 // 每小时
const DEFAULT_MAX_RETRIES = 5
```

系统默认每小时检查一次更新，以确保配置的及时性。

### 适用范围

- Console 用户 (API key): 默认适用
- OAuth 用户: 主要面向 Enterprise/C4E 和 Team 订阅者进行企业级管控

### 安全变更确认

当远程设置涉及关键或敏感的权限变更时，系统会弹出确认提示框：

```typescript
// src/services/remoteManagedSettings/securityCheck.tsx:67-73
export function handleSecurityCheckResult(result: SecurityCheckResult): boolean {
  if (result === 'rejected') {
    gracefulShutdownSync(1)  // 拒绝后安全退出
    return false
  }
  return true
}
```

为了保障环境安全，如果用户拒绝了必须的安全配置更新，程序将安全退出。这是一种常见的强制合规策略。

### 故障容灾

当远程服务器不可达时，系统会回退使用本地缓存的配置，保证基础功能的可用性。

## 2. 功能开关 (Feature Flags)

系统使用 GrowthBook feature flag 实现了灵活的功能管控，可以在发现严重问题时紧急禁用特定功能：

### 权限绕过功能管控

```typescript
// src/utils/permissions/bypassPermissionsKillswitch.ts
// 用于在必要时关闭"绕过权限"功能，防止安全风险
```

### 自动模式断路器

```typescript
// src/utils/permissions/autoModeState.ts
// autoModeCircuitBroken 状态用于在异常情况下暂停自动模式
```

### 快速模式开关

```typescript
// src/utils/fastMode.ts
// 从 /api/claude_code_penguin_mode 获取状态
// 动态管理快速模式的可用性
```

### 数据上报通道控制

```typescript
// src/services/analytics/sinkKillswitch.ts:4
const SINK_KILLSWITCH_CONFIG_NAME = 'tengu_frond_boric'
```

### 语音模式开关

```typescript
// src/voice/voiceModeEnabled.ts:21
// 'tengu_amber_quartz_disabled' — 用于在发现语音模块缺陷时紧急关闭
```

## 3. 模型覆盖系统

为了进行灰度测试或应对线上突发情况，系统支持对内部员工等特定群体进行模型版本的动态切换：

```typescript
// src/utils/model/antModels.ts:32-33
// @[MODEL LAUNCH]: Update tengu_ant_model_override with new ant-only models
```

`tengu_ant_model_override` GrowthBook flag 可以：
- 设置默认模型
- 设置默认 effort level
- 追加系统提示词
- 定义自定义模型别名

## 总结

| 机制 | 范围 | 用户同意 |
|------|------|---------|
| 远程托管设置 | Enterprise/Team | 接受或退出 |
| GrowthBook feature flags | 所有用户 | 无 |
| Kill switches | 所有用户 | 无 |
| 模型覆盖 | 内部 (ant) | 无 |
| 快速模式控制 | 所有用户 | 无 |

远程控制基础设施极其广泛，且在很大程度上没有用户可见性或同意机制。企业管理员可以强制执行用户无法覆盖的策略，Anthropic 可以通过 feature flag 远程更改任何用户的行为。


# FILE: docs/zh/05-未来路线图.md

# 未来路线图 — 架构揭示的方向

> 基于网络公开资料与社区讨论整理的 Claude Code v2.1.88 分析报告。

## 1. 下一代模型: Numbat

从公开资料中的架构推测来看：

```typescript
// 架构内部推断代码片段
// @[MODEL LAUNCH]: Remove this section when we launch numbat.
```

**Numbat（袋食蚁兽）** 似乎是即将发布的模型代号。资料暗示 Numbat 发布时可能会移除某些当前的输出控制逻辑，这意味着新模型可能有更好的原生输出能力。

### 未来版本号

公开的讨论中提到了一些可能的版本号：
- Unreleased model version numbers (e.g., opus-4-7, sonnet-4-8)

**Opus 4.7** 和 **Sonnet 4.8** 似乎正在开发中。

### 代号演化链

从社区的猜测来看，代号的演化链可能是：
```
Fennec（耳廓狐） → Opus 4.6 → [Numbat?]
Capybara（水豚） → Sonnet v8 → [?]
Tengu（天狗） → 遥测/产品前缀
```

### 模型发布清单

从网上整理的资料来看，架构中预留了许多 `@[MODEL LAUNCH]` 的标记，用于在未来新模型发布时更新配置，例如：
- 默认模型名称
- 知识截止日期
- 定价表
- 上下文窗口配置
- Thinking 模式支持
- 迁移脚本

## 2. KAIROS — 自主代理模式

被社区广泛讨论的未发布特性之一，KAIROS 似乎旨在将 Claude Code 从被动助手转变为主动自主代理。

### 行为预期（根据公开资料推测）

```text
# 预期系统逻辑
代理将处于自主运行状态。
系统可能通过心跳信号（如 <tick>）保持代理活跃。
如果没有有用的事可做，代理可能会调用休眠功能。
在适当的情况下，代理可能会主动行动——读取文件、做修改、提交，无需用户每次确认。
```

### 关联工具推测

根据公开的讨论，可能涉及以下工具：

| 工具 | 用途推测 |
|------|------|
| SleepTool | 控制自主操作间的节奏 |
| SendUserFileTool | 主动向用户发送文件 |
| PushNotificationTool | 推送通知到用户设备 |
| SubscribePRTool | 订阅 GitHub PR webhook 事件 |
| BriefTool | 主动状态更新 |

### 行为特征

- 通过心跳机制保持活跃
- 根据用户在终端的活跃状态调整自主程度
- 可以独立 commit、push 和做决策
- 发送主动通知和状态更新
- 监控代码仓库（如 GitHub）的变更

## 3. 语音模式

有资料显示，语音交互的基础设施可能已经在开发中，但目前尚未对外开放：

- **Push-to-Talk**: 可能实现类似对讲机的界面
- **Audio Capture**: 通过原生模块集成
- 仅限特定认证用户使用

## 4. 未上线工具

根据社区挖掘的信息，以下工具可能在开发计划中但尚未对外部用户开放：

| 工具 | 描述推测 |
|------|-------------|
| **WebBrowserTool** | 内置浏览器自动化，超越简单的网页抓取 |
| **TerminalCaptureTool** | 终端面板捕获和监控 |
| **WorkflowTool** | 执行预定义工作流脚本 |
| **MonitorTool** | 系统/进程监控 |
| **SnipTool** | 对话历史智能裁剪 |
| **ListPeersTool** | 用于代理间的对等发现 |

## 5. 协调器模式

多代理协调系统：

旨在支持多个代理之间的协调任务执行，可能具有共享状态和消息传递机制。

## 6. 虚拟宠物系统 (Buddy)

有传言称一个完整的虚拟宠物系统正在开发中，可能包含：

- **多种物种**: 如鸭子、鹅、猫、龙、章鱼等
- **不同稀有度**: 从普通到传说
- **个性化属性**: 如 DEBUGGING、PATIENCE 等
- 基于用户 ID 的确定性生成

## 7. 后台记忆整固

有资料提到一个类似"做梦"的后台任务，旨在使 AI 能在空闲时间自主处理和整固记忆。

## 总结：三大方向

从目前的公开资料来看，Claude Code 可能在以下几个方向演进：
1. **新模型**: Numbat（下一代）、Opus 4.7、Sonnet 4.8
2. **自主代理**: KAIROS 模式 — 无人值守运行、主动行动、推送通知
3. **多模态与自动化**: 语音输入、浏览器自动化、工作流自动化

Claude Code 似乎正计划从一个**编程助手**进化为一个**全天候自主开发代理**。


# FILE: docs/zh/03-卧底模式分析.md

# 卧底模式分析

> 基于网络公开资料与社区讨论整理的 Claude Code v2.1.88 分析报告。

## 什么是卧底模式？

卧底模式是供官方内部员工在外部/开源仓库工作时使用的一种安全防护机制。激活后，系统会隐藏内部特有的 AI 模型信息及归属标识，使提交的代码与人类开发者的贡献形式保持一致。此举主要为了防止内部机密和未发布模型的名称在开源社区中泄露。

来源: `src/utils/undercover.ts`

## 激活逻辑

```typescript
// src/utils/undercover.ts:28-37
export function isUndercover(): boolean {
  if (process.env.USER_TYPE === 'ant') {
    if (isEnvTruthy(process.env.CLAUDE_CODE_UNDERCOVER)) return true
    // 自动模式：除非确认在白名单内部仓库，否则默认激活
    return getRepoClassCached() !== 'internal'
  }
  return false
}
```

关键特性：
- **仅限内部**: 只对官方员工 (`USER_TYPE === 'ant'`) 生效
- **默认开启**: 在所有仓库中激活，除非在内部白名单上
- **无法强制关闭**: 为了防止模型代号泄露，没有提供关闭选项
- **外部构建**: 对普通用户版本不生效，相关代码在打包时会被消除

## 给模型的指令

```
## UNDERCOVER MODE — CRITICAL

You are operating UNDERCOVER in a PUBLIC/OPEN-SOURCE repository.
Do not blow your cover.

NEVER include in commit messages or PR descriptions:
- 内部模型代号（如 Capybara, Tengu 等动物名称）
- 未发布的模型版本号（如 opus-4-7, sonnet-4-8）
- 内部仓库或项目名（如 claude-cli-internal）
- 内部工具、Slack 频道或短链接
- "Claude Code" 这个词或任何你是 AI 的暗示
- 任何关于你是什么模型或版本的提示
- Co-Authored-By 行或任何其他归属

像人类开发者一样写 commit message。

好:
- "Fix race condition in file watcher initialization"

坏:
- "Fix bug found while testing with Claude Capybara"
- "Generated with Claude Code"
- "Co-Authored-By: Claude Opus 4.6 <…>"
```

关键词：**"Do not blow your cover"**（旨在要求模型隐藏其内部身份，确保不会在外部泄露未公开信息）。

## 归属系统

归属系统同样配合了这一模式：

```typescript
// src/utils/model/model.ts:386-392
function maskModelCodename(baseName: string): string {
  // capybara-v2-fast → cap*****-v2-fast
  const [codename = '', ...rest] = baseName.split('-')
  const masked = codename.slice(0, 3) + '*'.repeat(Math.max(0, codename.length - 3))
  return [masked, ...rest].join('-')
}
```

## 影响

### 对开源社区的影响

当官方员工使用 Claude Code 参与开源项目时：
1. 提交记录不会带有 "Co-Authored-By: Claude" 等明显的 AI 署名
2. 缺乏 "Generated with Claude Code" 等标记
3. 这在一定程度上模糊了代码是由 AI 辅助生成还是由人类直接编写的界限
4. 在开源社区中，有关 AI 贡献的透明度规范正在建立，这种做法可能引发一些关于透明度的讨论

### 对官方的保护

主要声明的目的是防止意外泄露公司机密：
- 内部模型代号（涉及竞争情报）
- 未发布的版本号（涉及产品发布节奏）
- 内部基础设施细节（涉及系统安全）

### 行业考量

"卧底模式" 这种设计展现了企业在保护商业机密与遵循开源透明度之间所面临的平衡挑战。在公开代码贡献中隐去 AI 身份，一方面有效防止了机密泄露，但另一方面也引发了业界关于代码归属透明度和贡献指南遵循情况的思考。


# FILE: docs/zh/02-隐藏功能与模型代号.md

# 隐藏功能与模型代号

> 基于网络公开资料与社区讨论整理的 Claude Code v2.1.88 分析报告。

## 模型代号体系

Anthropic 使用**动物名称**作为内部模型代号。这些代号被严格保护，防止泄露到外部构建中。

### 已知代号

| 代号 | 角色 | 证据 |
|------|------|------|
| **Tengu**（天狗） | 产品/遥测前缀，也可能是模型 | 所有 250+ 分析事件和 feature flag 使用 `tengu_*` 前缀 |
| **Capybara**（水豚） | Sonnet 系列模型，当前版本 v8 | `capybara-v2-fast[1m]`，v8 行为问题的 prompt 补丁 |
| **Fennec**（耳廓狐） | Opus 4.6 的前代 | 迁移: `fennec-latest` → `opus` |
| **Numbat**（袋食蚁兽） | 下一代模型 | 注释: "Remove this section when we launch numbat" |

### 代号保护机制

Undercover 模式明确列出了受保护的代号：

```typescript
// src/utils/undercover.ts:48-49
NEVER include in commit messages or PR descriptions:
- Internal model codenames (animal names like Capybara, Tengu, etc.)
- Unreleased model version numbers (e.g., opus-4-7, sonnet-4-8)
```

构建系统使用 `scripts/excluded-strings.txt` 扫描泄露的代号。Buddy 系统的物种通过 `String.fromCharCode()` 编码以避免触发金丝雀检查：

```typescript
// src/buddy/types.ts:10-13
// One species name collides with a model-codename canary in excluded-strings.txt.
// 运行时构造值，保持字面量不出现在构建产物中
```

那个冲突的物种就是 **capybara** — 既是宠物物种又是模型代号。

### Capybara v8 的行为问题

架构揭示了 Capybara v8 的具体行为问题：

1. **停止序列误触发** (~10% 概率) — prompt 尾部出现 `<functions>` 时
2. **空 tool_result 导致零输出** — 需要注入 marker workaround
3. **过度写注释** — 需要专门的反注释 prompt 补丁
4. **高虚假声明率**: v8 为 29-30%，而 v4 为 16.7%
5. **验证不足** — 需要 "thoroughness counterweight" 补丁

## Feature Flag 命名约定

所有 feature flag 使用 `tengu_` 前缀 + **随机词对**以掩盖用途：

| Flag | 用途 |
|------|------|
| `tengu_onyx_plover` | Auto Dream（后台记忆整理）|
| `tengu_coral_fern` | memdir 功能 |
| `tengu_herring_clock` | 团队内存 |
| `tengu_frond_boric` | 分析 kill switch |
| `tengu_amber_quartz_disabled` | 语音模式 kill switch |
| `tengu_amber_flint` | 代理团队 |

## 内外部用户的差异

Anthropic 员工 (`USER_TYPE === 'ant'`) 获得显著更好的待遇：

| 维度 | 外部用户 | 内部用户 (ant) |
|------|---------|--------------|
| 输出风格 | "尽量简洁" | "倾向于更多解释" |
| 虚假声明缓解 | 无 | 专门的 Capybara v8 补丁 |
| 数值长度锚定 | 无 | "工具间 ≤25 词，最终回复 ≤100 词" |
| 验证代理 | 无 | 非简单改动必须启用 |
| 主动性 | 无 | "发现用户误解要指出" |

## 隐藏命令

| 命令 | 状态 | 描述 |
|------|------|------|
| `/btw` | 活跃 | 顺带提问，不打断主对话 |
| `/stickers` | 活跃 | 订购 Claude Code 贴纸 |
| `/thinkback` | 活跃 | 2025 年度回顾 |
| `/good-claude` | 占位 | 隐藏的 stub 命令 |
| `/bughunter` | 占位 | 隐藏的 stub 命令 |


# FILE: docs/zh/01-遥测与隐私分析.md

# 遥测与隐私分析

> 基于网络公开资料与社区讨论整理的 Claude Code v2.1.88 分析报告。

## 概述

Claude Code 实现了双层分析管道，收集大量环境和使用元数据。虽然没有证据表明存在键盘记录或源代码窃取，但收集范围之广和无法完全退出的事实引发了合理的隐私担忧。

## 数据管道架构

### 第一方日志 (1P)

- **端点**: `https://api.anthropic.com/api/event_logging/batch`
- **协议**: OpenTelemetry + Protocol Buffers
- **批量大小**: 每批最多 200 个事件，每 10 秒刷新一次
- **重试机制**: 二次方退避，最多 8 次尝试，失败事件持久化到磁盘
- **存储位置**: `~/.claude/telemetry/`

来源: `src/services/analytics/firstPartyEventLoggingExporter.ts`

### 第三方日志 (Datadog)

- **端点**: `https://http-intake.logs.us5.datadoghq.com/api/v2/logs`
- **范围**: 仅限 64 种预批准事件类型
- **Token**: `pubbbf48e6d78dae54bceaa4acf463299bf`

来源: `src/services/analytics/datadog.ts`

## 收集了什么

### 环境指纹

每个事件都携带以下元数据 (`src/services/analytics/metadata.ts:417-452`)：

```
- platform, platformRaw, arch, nodeVersion
- 终端类型
- 已安装的包管理器和运行时
- CI/CD 检测、GitHub Actions 元数据
- WSL 版本、Linux 发行版、内核版本
- 版本控制系统类型
- Claude Code 版本和构建时间
- 部署环境
```

### 进程指标 (`metadata.ts:457-467`)

```
- 运行时间、rss、heapTotal、heapUsed
- CPU 使用率和百分比
- 内存占用详情
```

### 用户追踪 (`metadata.ts:472-496`)

```
- 正在使用的模型
- 会话 ID、用户 ID、设备 ID
- 账户 UUID、组织 UUID
- 订阅等级 (max, pro, enterprise, team)
- 仓库远程 URL 哈希 (SHA256 前 16 位)
- 代理类型、团队名、父会话 ID
```

### 工具输入日志

默认截断工具输入：

```
- 字符串: 512 字符处截断，显示 128 + 省略号
- JSON: 限制 4,096 字符
- 数组: 最多 20 项
- 嵌套对象: 最多 2 层
```

然而，当设置 `OTEL_LOG_TOOL_DETAILS=1` 时，**完整工具输入会被记录**。

### 文件扩展名追踪

涉及 `rm, mv, cp, touch, mkdir, chmod, chown, cat, head, tail, sort, stat, diff, wc, grep, rg, sed` 的 Bash 命令，其文件参数的扩展名会被提取并记录。

## 无法退出的问题

第一方日志管道**无法被关闭**（对于直接使用 Anthropic API 的用户）。

`isAnalyticsDisabled()` 仅在以下情况返回 true：
- 测试环境
- 第三方云提供商 (Bedrock, Vertex)
- 全局遥测退出（设置界面未暴露此选项）

**没有面向用户的设置可以禁用第一方事件日志。**

## GrowthBook A/B 测试

用户在不知情的情况下被分配到实验组。系统发送的用户属性包括：

```
- id, sessionId, deviceID
- platform, organizationUUID, subscriptionType
```

## 关键结论

1. **体量**: 每个会话收集数百个事件
2. **无法退出**: 直接 API 用户无法禁用第一方日志
3. **持久化**: 失败事件保存到磁盘并积极重试
4. **第三方共享**: 数据发送到 Datadog
5. **工具详情后门**: `OTEL_LOG_TOOL_DETAILS=1` 启用完整输入记录
6. **仓库指纹**: 仓库 URL 被哈希后发送用于服务端关联


# FILE: docs/ko/02-숨겨진-기능과-코드네임.md

# 숨겨진 기능과 모델 코드네임

> 인터넷에 공개된 자료와 커뮤니티 토론을 바탕으로 정리된 Claude Code v2.1.88 분석 보고서.

## 모델 코드네임 체계

Anthropic은 내부 모델 코드네임으로 **동물 이름**을 사용한다. 외부 빌드로의 유출을 적극적으로 차단하고 있다.

### 알려진 코드네임

| 코드네임 | 역할 | 근거 |
|----------|------|------|
| **Tengu** (천구) | 제품/텔레메트리 접두사, 모델일 가능성 있음 | 250개 이상의 분석 이벤트 및 feature flag에 `tengu_*` 접두사로 사용 |
| **Capybara** (카피바라) | Sonnet 계열 모델, 현재 v8 | `capybara-v2-fast[1m]`, v8 동작 문제 패치 존재 |
| **Fennec** (페넥여우) | Opus 4.6 이전 모델 | 마이그레이션: `fennec-latest` → `opus` |
| **Numbat** (넘뱃) | 차기 모델 출시 예정 | 주석: "Remove this section when we launch numbat" |

### 코드네임 보호

`undercover` 모드에서 보호 대상 코드네임이 명시적으로 나열되어 있다:

```typescript
// src/utils/undercover.ts:48-49
NEVER include in commit messages or PR descriptions:
- Internal model codenames (animal names like Capybara, Tengu, etc.)
- Unreleased model version numbers (e.g., opus-4-7, sonnet-4-8)
```

빌드 시스템은 `scripts/excluded-strings.txt`를 사용하여 유출된 코드네임을 검출한다. Buddy 시스템의 종(species)은 `String.fromCharCode()`로 인코딩하여 canary 검출을 우회한다:

```typescript
// src/buddy/types.ts:10-13
// One species name collides with a model-codename canary in excluded-strings.txt.
// The check greps build output (not source), so runtime-constructing the value keeps
// the literal out of the bundle while the check stays armed for the actual codename.
```

충돌하는 종은 **capybara** — 펫 종이자 모델 코드네임이다.

### Capybara 동작 이슈 (v8)

아키텍처에서 Capybara v8의 구체적 동작 문제가 확인된다:

1. **Stop sequence 오발동** (프롬프트 끝에 `<functions>` 있을 때 ~10% 발생)
   - 출처: `src/utils/messages.ts:2141`

2. **빈 tool_result 시 출력 없음**
   - 출처: `src/utils/toolResultStorage.ts:281`

3. **과도한 주석 삽입** — 전용 주석 방지 프롬프트 패치 필요
   - 출처: `src/constants/prompts.ts:204`

4. **높은 허위 주장 비율**: v8은 29-30%, v4는 16.7%
   - 출처: `src/constants/prompts.ts:237`

5. **불충분한 검증** — "철저함 보정값(thoroughness counterweight)" 필요
   - 출처: `src/constants/prompts.ts:210`

## Feature Flag 명명 규칙

모든 feature flag는 `tengu_` 접두사에 **무작위 단어 조합**을 사용하여 목적을 난독화한다:

| Flag | 용도 |
|------|------|
| `tengu_onyx_plover` | Auto Dream (백그라운드 기억 통합) |
| `tengu_coral_fern` | memdir 기능 |
| `tengu_moth_copse` | memdir 추가 스위치 |
| `tengu_herring_clock` | Team memory |
| `tengu_passport_quail` | Path 기능 |
| `tengu_slate_thimble` | memdir 추가 스위치 |
| `tengu_sedge_lantern` | Away Summary |
| `tengu_frond_boric` | 분석 킬스위치 |
| `tengu_amber_quartz_disabled` | 음성 모드 킬스위치 |
| `tengu_amber_flint` | Agent teams |
| `tengu_hive_evidence` | 검증 에이전트 |

무작위 단어 패턴(형용사/재질 + 자연/사물)은 외부 관찰자가 flag 이름만으로 기능 목적을 추론하는 것을 방지한다.

## 내부 사용자와 외부 사용자 차이

Anthropic 직원(`USER_TYPE === 'ant'`)은 상당히 다른 대우를 받는다:

### 프롬프트 차이 (`src/constants/prompts.ts`)

| 항목 | 외부 사용자 | 내부 사용자 (ant) |
|------|------------|------------------|
| 출력 스타일 | "Be extra concise" (극도로 간결하게) | "Err on the side of more explanation" (설명을 더 하는 쪽으로) |
| 허위 주장 대응 | 없음 | 전용 Capybara v8 패치 적용 |
| 수치적 길이 기준 | 없음 | "도구 사이 ≤25단어, 최종 답변 ≤100단어" |
| 검증 에이전트 | 없음 | 비자명한 변경에 필수 적용 |
| 주석 가이드 | 일반적 | 전용 과잉 주석 방지 프롬프트 |
| 선제적 교정 | 없음 | "사용자에게 오해가 있으면 지적" |

### 도구 접근

내부 사용자만 접근 가능한 도구:
- `REPLTool` — REPL 모드
- `SuggestBackgroundPRTool` — 백그라운드 PR 제안
- `TungstenTool` — 성능 모니터링 패널
- `VerifyPlanExecutionTool` — 계획 실행 검증
- Agent 중첩 (에이전트가 에이전트를 생성)

## 숨겨진 명령어

| 명령어 | 상태 | 설명 |
|--------|------|------|
| `/btw` | 활성 | 작업 중단 없이 곁다리 질문 |
| `/stickers` | 활성 | Claude Code 스티커 주문 (브라우저 열림) |
| `/thinkback` | 활성 | 2025 연말 회고 |
| `/effort` | 활성 | 모델 노력 수준 설정 |
| `/good-claude` | 스텁 | 숨겨진 플레이스홀더 |
| `/bughunter` | 스텁 | 숨겨진 플레이스홀더 |


# FILE: docs/ko/03-언더커버-모드.md

# 언더커버 모드 분석

> 인터넷에 공개된 자료와 커뮤니티 토론을 바탕으로 정리된 Claude Code v2.1.88 분석 보고서.

## 언더커버 모드란?

언더커버 모드는 공식 직원이 외부/오픈소스 저장소에서 작업할 때 사용되는 안전 보호 메커니즘입니다. 활성화되면 내부 특화 AI 모델 정보와 저작 표시를 숨겨 제출된 코드가 인간 개발자의 기여와 동일하게 보이도록 합니다. 이는 주로 내부 기밀 및 미출시 모델의 이름이 오픈소스 커뮤니티에 유출되는 것을 방지하기 위함입니다.

출처: `src/utils/undercover.ts`

## 활성화 조건

```typescript
// src/utils/undercover.ts:28-37
export function isUndercover(): boolean {
  if (process.env.USER_TYPE === 'ant') {
    if (isEnvTruthy(process.env.CLAUDE_CODE_UNDERCOVER)) return true
    // Auto: 내부 저장소로 확인되지 않으면 자동 활성화
    return getRepoClassCached() !== 'internal'
  }
  return false
}
```

주요 특성:
- **내부 전용**: 공식 직원(`USER_TYPE === 'ant'`)만 해당
- **기본 활성화**: 내부 허용 목록에 없는 모든 저장소에서 자동 활성화
- **강제 비활성화 불가**: "There is NO force-OFF. This guards against model codename leaks"
- **외부 빌드**: 번들러에 의해 데드 코드 제거됨; 실행되지 않음

## 모델에 전달되는 프롬프트

```typescript
// src/utils/undercover.ts:39-69
export function getUndercoverInstructions(): string {
  return `## UNDERCOVER MODE — CRITICAL

You are operating UNDERCOVER in a PUBLIC/OPEN-SOURCE repository. Your commit
messages, PR titles, and PR bodies MUST NOT contain ANY Anthropic-internal
information. Do not blow your cover.

NEVER include in commit messages or PR descriptions:
- Internal model codenames (animal names like Capybara, Tengu, etc.)
- Unreleased model version numbers (e.g., opus-4-7, sonnet-4-8)
- Internal repo or project names (e.g., claude-cli-internal, anthropics/…)
- Internal tooling, Slack channels, or short links (e.g., go/cc, #claude-code-…)
- The phrase "Claude Code" or any mention that you are an AI
- Any hint of what model or version you are
- Co-Authored-By lines or any other attribution

Write commit messages as a human developer would — describe only what the code
change does.

GOOD:
- "Fix race condition in file watcher initialization"
- "Add support for custom key bindings"

BAD (never write these):
- "Fix bug found while testing with Claude Capybara"
- "1-shotted by claude-opus-4-6"
- "Generated with Claude Code"
- "Co-Authored-By: Claude Opus 4.6 <…>"`
}
```

## 저작 표시 시스템

저작 표시 시스템(`src/utils/attribution.ts`, `src/utils/commitAttribution.ts`)은 언더커버 모드를 보완한다:

```typescript
// src/utils/attribution.ts:70-72
// @[MODEL LAUNCH]: 아래 하드코딩된 폴백 모델 이름 업데이트
// (코드네임 유출 방지용).
// 외부 저장소에서 인식되지 않는 모델은 "Claude Opus 4.6"으로 폴백.
```

```typescript
// src/utils/model/model.ts:386-392
function maskModelCodename(baseName: string): string {
  // e.g. capybara-v2-fast → cap*****-v2-fast
  const [codename = '', ...rest] = baseName.split('-')
  const masked = codename.slice(0, 3) + '*'.repeat(Math.max(0, codename.length - 3))
  return [masked, ...rest].join('-')
}
```

## 시사점

### 오픈소스에 대한 영향

공식 직원이 Claude Code로 오픈소스 프로젝트에 기여할 때:
1. AI가 코드를 작성하지만 커밋은 사람이 작성한 것으로 표시된다
2. "Co-Authored-By: Claude" 저작 표시가 없다
3. "Generated with Claude Code" 마커가 없다
4. 프로젝트 메인테이너와 커뮤니티는 AI 생성 기여를 식별할 수 없다
5. 이는 AI 기여에 관한 오픈소스 투명성 규범을 잠재적으로 위반한다

### 공식 보호 목적

명시된 주요 목적은 다음의 우발적 유출 방지:
- 내부 모델 코드네임 (경쟁 정보)
- 미공개 버전 번호 (시장 타이밍)
- 내부 인프라 세부 정보 (보안)

### 윤리적 고려사항

"Do not blow your cover(정체를 들키지 마라)"라는 표현은 AI를 잠입 요원으로 프레이밍한다. 공개 코드 기여에서의 의도적인 AI 저작 은폐는 다음과 같은 질문을 제기한다:
- 오픈소스 커뮤니티에서의 투명성
- 프로젝트 기여 가이드라인 준수 여부
- 영업비밀 보호와 기만 사이의 경계

