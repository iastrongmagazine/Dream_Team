# Brand.json Schema

```json
{
  "name": "Brand Name",
  "tagline": "Brand tagline",
  "colors": {
    "primary": "#XXXXXX",
    "secondary": "#XXXXXX",
    "accent": "#XXXXXX",
    "background": "#XXXXXX",
    "text": "#XXXXXX"
  },
  "fonts": {
    "heading": "Font Name",
    "body": "Font Name",
    "mono": "Font Name"
  },
  "logo": {
    "main": "path/to/logo.svg",
    "icon": "path/to/icon.svg"
  },
  "audience": {
    "primary": "Description of primary audience",
    "pain_points": ["pain1", "pain2"],
    "goals": ["goal1", "goal2"]
  },
  "values": ["value1", "value2", "value3"]
}
```

## Required Fields
- name
- colors.primary
- fonts.heading
- fonts.body
- audience.primary

## Optional Fields
- tagline
- logo
- values
