# Frontend Guidelines

面向人类开发者与 AI Agent 的通用前端工程规范。

本仓库定义**应该实现什么体验、如何选择交互模式、如何验证结果**，但不提供任何 UI 组件、框架适配层或样式代码。规范可用于 React、Vue、Svelte、原生 Web 或其他前端技术栈。

## 这是什么

它是一套可执行的前端开发契约，覆盖：

- 页面结构与视觉层级；
- 表单、弹层、导航、数据展示、筛选和反馈模式；
- 响应式、键盘、焦点和中文输入法行为；
- 面向用户的文案边界；
- AI 修改前端时的工作流程；
- 完成后的验收与回归检查。

## 这不是什么

本仓库**不是**：

- UI 组件库；
- 设计 Token 包；
- 某个框架的脚手架；
- 某个 UI 库的使用手册；
- 可复制到项目中的业务代码。

规范禁止依赖具体组件名称、CSS 类名或某个框架的 API 来表达要求。

## AI 从哪里开始

AI Agent 必须按以下顺序阅读：

1. [`AGENTS.md`](AGENTS.md)：执行入口与规则优先级；
2. [`FRONTEND_SPEC.md`](FRONTEND_SPEC.md)：强制规则的紧凑版本；
3. 与当前任务相关的 [`docs/`](docs/) 章节；
4. [`docs/10-validation-checklist.md`](docs/10-validation-checklist.md)：完成前检查。

不需要每次读取全部文件。先根据任务范围选择相关章节，但 `AGENTS.md` 和 `FRONTEND_SPEC.md` 始终必读。

## 在项目中接入

推荐将本仓库固定到明确版本，放到项目内可被 Agent 直接读取的位置：

```text
docs/frontend-guidelines/
```

可以使用 Git submodule、subtree，或在项目初始化时复制一份。不要只在项目文档中放远程链接，因为执行环境可能没有网络访问。

随后将 [`templates/PROJECT_AGENTS_SNIPPET.md`](templates/PROJECT_AGENTS_SNIPPET.md) 的内容加入项目根目录 `AGENTS.md`，并填写 [`templates/PROJECT_FRONTEND_PROFILE.md`](templates/PROJECT_FRONTEND_PROFILE.md)。

项目自身的明确业务约束高于本通用规范；任何偏离都必须在项目 Profile 中记录原因、影响范围和验证方式。

## 规则表达

规范使用以下等级：

- **MUST**：必须遵守；
- **MUST NOT**：禁止；
- **SHOULD**：除非有明确理由，否则应遵守；
- **MAY**：可选。

每条强制规则都有稳定 ID，例如 `FG-OVERLAY-002`，便于 AI 在方案、提交信息和评审中引用。

## 仓库结构

```text
AGENTS.md                 AI 执行入口与优先级
FRONTEND_SPEC.md          45 条带稳定 ID 的规范
docs/                     按主题展开的解释与验收方法
examples/                 与框架无关的正确/错误示意
templates/                项目接入与偏离记录模板
scripts/validate.py       纯文档边界和链接检查
```

## 版本

当前版本见 [`VERSION`](VERSION)。版本变更遵循语义化版本：

- PATCH：澄清文字，不改变要求；
- MINOR：增加兼容的新规则；
- MAJOR：删除规则或改变既有规则含义。

## 许可证

[MIT](LICENSE)
