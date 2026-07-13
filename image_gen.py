#!/usr/bin/env python3
"""
Professional Infographic Generator for Claude Code Skills
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_claude_code_skills_infographic():
    # Infographic dimensions (tall format for comprehensive info)
    width = 1200
    height = 1800

    # Color scheme - professional blues and grays
    colors = {
        'background': '#1a1a2e',
        'header_bg': '#16213e',
        'accent': '#e94560',
        'primary': '#0f3460',
        'text_white': '#ffffff',
        'text_light': '#a8a8a8',
        'card_bg': '#1f2937',
        'highlight': '#4fd1c5'
    }

    # Create image
    img = Image.new('RGB', (width, height), colors['background'])
    draw = ImageDraw.Draw(img)

    # Try to use system fonts, fallback to default
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        heading_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
        body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
        code_font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 20)
    except:
        title_font = ImageFont.load_default()
        heading_font = title_font
        body_font = title_font
        small_font = title_font
        code_font = title_font

    y_pos = 40

    # Header section
    draw.rectangle([0, 0, width, 140], fill=colors['header_bg'])
    draw.text((width//2, 50), "CLAUDE CODE SKILLS", font=title_font, fill=colors['text_white'], anchor="mm")
    draw.text((width//2, 100), "Your Complete Guide to Slash Commands", font=body_font, fill=colors['text_light'], anchor="mm")

    # Accent line
    draw.rectangle([100, 145, width-100, 150], fill=colors['accent'])

    y_pos = 180

    # What are Skills section
    draw.rounded_rectangle([50, y_pos, width-50, y_pos+120], radius=15, fill=colors['card_bg'])
    draw.text((80, y_pos+20), "What are Claude Code Skills?", font=heading_font, fill=colors['highlight'])
    draw.text((80, y_pos+65), "Skills are pre-built commands (slash commands) that automate", font=small_font, fill=colors['text_light'])
    draw.text((80, y_pos+90), "common workflows. Invoke them with /<skill-name>", font=small_font, fill=colors['text_light'])

    y_pos += 150

    # Built-in Skills section
    skills_data = [
        {
            'name': '/commit',
            'desc': 'Stage and commit changes with AI-generated messages',
            'example': 'Review changes, generate semantic commit message'
        },
        {
            'name': '/review-pr',
            'desc': 'Get comprehensive code review on pull requests',
            'example': '/review-pr 123 or /review-pr <url>'
        },
        {
            'name': '/feature-dev',
            'desc': 'Guided feature development with architecture focus',
            'example': 'Plan and implement features systematically'
        },
        {
            'name': '/implement-design',
            'desc': 'Convert Figma designs to production code',
            'example': 'Requires Figma MCP server connection'
        }
    ]

    draw.text((80, y_pos), "Popular Built-in Skills", font=heading_font, fill=colors['accent'])
    y_pos += 50

    for skill in skills_data:
        draw.rounded_rectangle([50, y_pos, width-50, y_pos+110], radius=12, fill=colors['primary'])
        draw.text((80, y_pos+15), skill['name'], font=code_font, fill=colors['highlight'])
        draw.text((80, y_pos+50), skill['desc'], font=small_font, fill=colors['text_white'])
        draw.text((80, y_pos+80), f"→ {skill['example']}", font=small_font, fill=colors['text_light'])
        y_pos += 125

    y_pos += 20

    # How to Use section
    draw.rounded_rectangle([50, y_pos, width-50, y_pos+200], radius=15, fill=colors['card_bg'])
    draw.text((80, y_pos+20), "How to Use Skills", font=heading_font, fill=colors['highlight'])

    steps = [
        "1. Type the skill name (e.g., /commit)",
        "2. Add optional arguments if needed",
        "3. Claude executes the specialized workflow",
        "4. Review and approve actions as prompted"
    ]

    step_y = y_pos + 65
    for step in steps:
        draw.text((100, step_y), step, font=body_font, fill=colors['text_white'])
        step_y += 35

    y_pos += 230

    # Custom Skills section
    draw.rounded_rectangle([50, y_pos, width-50, y_pos+180], radius=15, fill=colors['header_bg'])
    draw.text((80, y_pos+20), "Create Custom Skills", font=heading_font, fill=colors['accent'])
    draw.text((80, y_pos+65), "Define your own skills in .claude/settings.json:", font=small_font, fill=colors['text_light'])

    code_example = '"skills": [{ "name": "deploy", "prompt": "..." }]'
    draw.text((100, y_pos+110), code_example, font=code_font, fill=colors['highlight'])
    draw.text((80, y_pos+150), "Custom skills appear alongside built-in commands", font=small_font, fill=colors['text_light'])

    y_pos += 210

    # Pro Tips section
    draw.text((80, y_pos), "Pro Tips", font=heading_font, fill=colors['accent'])
    y_pos += 45

    tips = [
        "Use /help to see all available skills",
        "Skills work with MCP servers for extended functionality",
        "Combine skills with hooks for automated workflows",
        "Check skill docs with: claude --help"
    ]

    for i, tip in enumerate(tips):
        bullet_color = colors['highlight'] if i % 2 == 0 else colors['accent']
        draw.ellipse([70, y_pos+8, 85, y_pos+23], fill=bullet_color)
        draw.text((100, y_pos), tip, font=body_font, fill=colors['text_white'])
        y_pos += 40

    # Footer
    draw.rectangle([0, height-60, width, height], fill=colors['header_bg'])
    draw.text((width//2, height-35), "Generated with Claude Code  |  anthropic.com", font=small_font, fill=colors['text_light'], anchor="mm")

    # Save the infographic
    output_path = os.path.join(os.path.dirname(__file__), 'claude_code_skills_infographic.png')
    img.save(output_path, 'PNG', quality=95)
    print(f"✓ Infographic saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    create_claude_code_skills_infographic()
