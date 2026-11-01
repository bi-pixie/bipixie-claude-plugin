# BI Pixie for Claude

BI Pixie for Claude helps Claude answer questions about Power BI and Microsoft Fabric
semantic models. Before Claude writes a query, it asks BI Pixie which measures, columns and
values people actually use in their reports. Claude then starts from the fields the
business relies on, and avoids look-alike measures and fields that nobody uses.

The plugin holds one skill and the BI Pixie connector. It is free, and it works on every
BI Pixie plan, Free included.

## What you need

- BI Pixie, in either of its two versions. BI Pixie records how people use the reports
  built on your semantic models.
  - **BI Pixie Cloud**, at https://app.bipixie.com.
  - **The BI Pixie workload in Microsoft Fabric**, with a BI Pixie item in one of your
    Fabric workspaces. You do not need a BI Pixie Cloud account.
- Access in Power BI to the semantic models you want Claude to read. Claude reads and
  queries them as you, with your row-level security.

## How to use it

**Claude in the browser, Claude Desktop and Cowork.** Install the plugin, then connect the
BI Pixie connector when Claude asks, and sign in with your work account. Ask a question
such as "What was revenue by region last quarter in the Sales semantic model?"

The **Use BI Pixie in Claude** card on the AI Assistants page shows the connector address
for your account, in case Claude asks for one. In BI Pixie Cloud, the AI Assistants page is
in the portal at https://app.bipixie.com. With the workload, open your BI Pixie item in
Microsoft Fabric, and the AI Assistants page is in the item.

**Claude Code.** Install the plugin with these two commands:

```
/plugin marketplace add bi-pixie/bipixie-claude-plugin
/plugin install bipixie@bipixie
```

When Claude Code asks, give it your Microsoft Entra tenant ID and the name of the Power BI
workspace that holds your BI Pixie Dashboard semantic model. With the workload, that is
the Fabric workspace where you created the BI Pixie item. Claude Code runs the local
BI Pixie server (`uvx bipixie-mcp==0.10.0`, MIT licensed), which signs you in through the Azure
CLI, so run `az login` first. You also need `uv` installed. In Claude Code the hosted
connector shows as not connected, because it answers only Claude's own cloud; the local
server is the Claude Code path.

Claude Code also asks for the BI Pixie API application ID. It is optional, and it lets the
local server manage BI Pixie for you, such as running a benchmark. For BI Pixie Cloud and
the workload, enter `114a7e20-3796-4ddd-ab99-568a78b7759b`. It is a public ID, not a
password. Left empty, the local server still answers questions about your data.

## What data it sends

- **The hosted connector** sends your question's tool calls to BI Pixie at
  `https://mcp.bipixie.com/mcp`. BI Pixie runs the query in Power BI as you and returns the
  result to Claude. BI Pixie keeps a record of each query (which tool, which fields, how
  many rows) and never keeps the values it returns.
- **The local server** runs on your own computer and calls Power BI and the BI Pixie API
  directly, as you.
- **Usage data** comes back as counts and rankings. The skill tells Claude not to ask for
  the names of the people who viewed a report.
- **Changes** such as starting a benchmark always show a preview first, and run only after
  you agree.

Privacy policy: https://bipixie.com/privacy. Terms: https://bipixie.com/terms-of-service.
Documentation for BI Pixie Cloud: https://bipixie.com/docs/cloud/ai-assistants/claude.
Documentation for the workload: https://bipixie.com/docs/fabric-workload/ai-assistants/claude.
Support: https://bipixie.com/support.

## License

MIT. See `LICENSE`.
