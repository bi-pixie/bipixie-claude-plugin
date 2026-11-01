# BI Pixie for Claude

BI Pixie for Claude helps Claude answer questions about Power BI and Microsoft Fabric
semantic models. Before Claude writes a query, it asks BI Pixie which measures, columns and
values people actually use in their reports. Claude then starts from the fields the
business relies on, and avoids look-alike measures and fields that nobody uses.

The plugin holds one skill and the BI Pixie connector. It is free, and it works on every
BI Pixie plan, Free included.

## What you need

- A BI Pixie account, at https://app.bipixie.com. BI Pixie records how people use the
  reports built on your semantic models.
- Access in Power BI to the semantic models you want Claude to read. Claude reads and
  queries them as you, with your row-level security.

## How to use it

**Claude in the browser, Claude Desktop and Cowork.** Install the plugin, then connect the
BI Pixie connector when Claude asks, and sign in with your work account. Ask a question
such as "What was revenue by region last quarter in the Sales semantic model?"

**Claude Code.** Install the plugin with these two commands:

```
/plugin marketplace add bi-pixie/bipixie-claude-plugin
/plugin install bipixie@bipixie
```

When Claude Code asks, give it your Microsoft Entra tenant ID and the name of the Power BI
workspace that holds your BI Pixie Dashboard semantic model. Claude Code runs the local
BI Pixie server (`uvx bipixie-mcp`, MIT licensed), which signs you in through the Azure
CLI, so run `az login` first. You also need `uv` installed. In Claude Code the hosted
connector shows as not connected, because it answers only Claude's own cloud; the local
server is the Claude Code path.

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
Documentation: https://bipixie.com/docs/cloud/ai-assistants/claude. Support: https://bipixie.com/support.

## License

MIT. See `LICENSE`.
