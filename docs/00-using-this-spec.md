# 使用这套规范

## 最小阅读集

任何前端任务都必须读取：

- 根目录 `AGENTS.md`；
- 根目录 `FRONTEND_SPEC.md`；
- 与任务相关的详细章节；
- 完成前的验证清单。

## 按任务选择章节

| 任务 | 必读章节 |
| --- | --- |
| 页面重构、间距、层级 | `01-principles.md`、`02-layout-and-hierarchy.md` |
| 表单、搜索、输入焦点 | `03-forms-and-input.md` |
| Dialog、Drawer、Select、Tooltip | `04-overlays-and-floating-ui.md` |
| Sidebar、导航、路由状态 | `05-navigation.md` |
| 加载、空、错误、通知 | `06-feedback-and-status.md` |
| 表格、列表、搜索、筛选 | `12-data-lists-and-filters.md` |
| 按钮、图标操作、操作层级 | `13-actions-and-controls.md` |
| 移动端、键盘、可访问性 | `07-responsive-and-accessibility.md` |
| 页面文案、按钮名称 | `08-content-language.md` |
| 实施与交付 | `09-implementation-workflow.md`、`10-validation-checklist.md` |

## 项目 Profile

项目应维护 `PROJECT_FRONTEND_PROFILE.md`，记录：

- 产品类型和主要用户；
- 框架与现有 UI 体系；
- 已采用的通用模式；
- 项目特有约束；
- 对本规范的临时偏离。

AI 不得用通用规范覆盖项目明确且合理的业务约束。

## 引用规则

方案和评审中优先引用规则 ID：

```text
根因违反 FG-FORM-002 和 FG-FORM-003。
修复位于共享搜索输入层，并验证中文组合输入与焦点稳定性。
```

引用规则不等于完成验证。必须同时说明证据。
