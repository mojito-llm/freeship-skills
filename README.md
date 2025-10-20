# FreeShip Skills

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks for the AIGC Film Production Factory.

For more information about skills, check out:
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

# About This Repository

This repository contains skills for the FreeShip AIGC Film Production Factory ecosystem. These skills extend Claude's capabilities for video production, content creation, and workflow automation tasks.

Each skill is self-contained in its own directory with a `SKILL.md` file containing the instructions and metadata that Claude uses.

**Note:** These skills are tailored for the FreeShip project workflows. Feel free to use them as inspiration for your own skills.

# Available Plugins

This repository is organized by AIGC film production workflow stages. Install only the plugin packages you need for your workflow.

## 🔧 common-skills
**公共工具技能** - General utility skills used across all production stages.

### sayhello
Generate friendly greetings in multiple languages and styles. Supports English, Chinese, Japanese, Spanish, French with formal/casual/professional styles and context-aware templates for business, email, and social situations.

---

## 🔍 parsing-skills *(coming soon)*
**解析技能** - Video platform parsing, content extraction, and metadata analysis.

**Planned skills:**
- Video URL parser (TikTok, 抖音, YouTube)
- Metadata extractor
- Thumbnail analyzer
- Audio extraction

---

## ✍️ scriptwriting-skills *(coming soon)*
**编剧技能** - AI-powered script generation, story optimization, and content planning.

**Planned skills:**
- AI script generator
- Story structure analyzer
- Storyboard creator
- Copywriting assistant
- Character development
- Dialogue optimizer

---

## 🎬 shooting-skills *(coming soon)*
**拍摄技能** - Shot planning, scene design, and filming guidance.

**Planned skills:**
- Shot list generator
- Scene planning assistant
- Camera angle recommender
- Lighting setup guide
- Asset management

---

## 🎞️ production-skills *(coming soon)*
**制片技能** - Post-production, editing, effects, and publishing.

**Planned skills:**
- Video editing assistant
- Subtitle generator
- AI voiceover
- Music composer
- Effects library
- Export optimizer
- Multi-platform publisher

---

## 🤖 llm-skills *(coming soon)*
**大模型调用技能** - LLM API integration, prompt engineering, and multi-model orchestration.

**Planned skills:**
- LLM API caller (OpenAI, Anthropic, DeepSeek, etc.)
- Prompt template manager
- Multi-model orchestrator
- Response parser & validator
- Token optimizer
- Streaming response handler
- Model comparison tool
- Cost tracker

# Try in Claude Code, Claude.ai, and the API

## Claude Code

### Local Installation (Recommended for Development)

1. **Add local marketplace:**
   ```bash
   /plugin marketplace add /Users/larrykoo/Documents/vibecoding/kimlab-project/freeship-skills
   ```

2. **Install plugin packages by workflow stage:**
   ```bash
   # 公共工具 (已可用)
   /plugin install common-skills@freeship-skills

   # 解析技能 (即将推出)
   /plugin install parsing-skills@freeship-skills

   # 编剧技能 (即将推出)
   /plugin install scriptwriting-skills@freeship-skills

   # 拍摄技能 (即将推出)
   /plugin install shooting-skills@freeship-skills

   # 制片技能 (即将推出)
   /plugin install production-skills@freeship-skills

   # 大模型调用技能 (即将推出)
   /plugin install llm-skills@freeship-skills
   ```

3. **Use the skills:**
   After installing, you can use skills by mentioning them. For example:
   - "Use the sayhello skill to generate a formal Chinese business greeting"
   - "帮我生成一个正式的商务邮件问候语"

### GitHub Installation (For Production)

```bash
# Add GitHub repository as marketplace
/plugin marketplace add your-org/freeship-skills

# Install plugins
/plugin install common-skills@freeship-skills
```

## Claude.ai

To use or upload custom skills, follow the instructions in [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_a4222fa77b).

## Claude API

You can upload custom skills via the Claude API. See the [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill) for more.

# Creating a Basic Skill

Skills are simple to create - just a folder with a `SKILL.md` file containing YAML frontmatter and instructions. You can use the **template-skill** in this repository as a starting point:

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

The frontmatter requires two fields:
- `name` - A unique identifier for your skill (lowercase, hyphens for spaces)
- `description` - A complete description of what the skill does and when to use it

The markdown content below contains the instructions, examples, and guidelines that Claude will follow. For more details, see [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) or review the `agent_skills_spec.md` file in this repository.

# Project Context

FreeShip Skills is part of the AIGC Film Production Factory ecosystem:

- **freeship** - Next.js frontend application for production management
- **freeship-agent** - MCP tools for video parsing, downloading, and processing
- **freeship-skills** - Claude Code skills for workflow automation (this repository)

# Contributing

When creating new skills for this repository:

1. Use `template-skill/` as a starting point
2. Focus on reusable workflows and common production tasks
3. Include clear examples and documentation
4. Test thoroughly before committing
5. Follow the Agent Skills Spec conventions (see `agent_skills_spec.md`)

---

**FreeShip AIGC Film Production Factory** - Internal Skills Repository
