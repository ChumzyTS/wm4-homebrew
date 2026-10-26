# WM4 Homebrew

A curated compilation of the **UTD TTRPG Club's Westmarch (WM4) D&D 5e homebrew content**, organized for use with [5e.tools](https://5e.tools).

This repository makes the Westmarch UTD homebrew catalog easier to browse and search, bringing custom content into one searchable collection.

The catalog includes items, spells, perks, talents, gifts, curses, conditions, and other homebrew content created by various creators, designed for use with 5e.tools.

## Features

- **Centralized catalog:** Consolidates Westmarch UTD homebrew content into a single searchable collection.
- **Broad content coverage:** Includes custom equipment, spells, character options, conditions, and other supported homebrew categories.
- **5e.tools integration:** Provides a compiled JSON file that can be loaded directly through the Homebrew Manager.
- **Data organization:** Stores content in category-specific JSON files for easier maintenance.
- **Python utilities:** Includes scripts for compiling catalog data, sorting entries, and supporting content conversion workflows.

## Getting Started

You do not need to clone this repository to use the catalog in 5e.tools. Follow the steps below to load it directly.

### Step 1: Open the Homebrew Manager

1. Visit [5e.tools](https://5e.tools).
2. From the home page, navigate to **Utilities → Homebrew Manager**.

### Step 2: Load the Catalog from URL

1. In the Homebrew Manager, select **Load from URL**.
2. Paste the following URL:

   **[Load the WM4 Homebrew JSON](https://raw.githubusercontent.com/ChumzyTS/wm4-homebrew/refs/heads/main/wm4-homebrew.json)**

   Direct URL:

   ```text
   https://raw.githubusercontent.com/ChumzyTS/wm4-homebrew/refs/heads/main/wm4-homebrew.json
   ```

3. Click **OK** to import the catalog.

If the import succeeds, the catalog should appear in the list as **Westmarch UTD**.

### Step 3: Verify the Catalog

1. Navigate to the Items section in 5e.tools.
2. Open the filter options.
3. Look under **Homebrew** for **Westmarch UTD**.

Once loaded, you can browse and search the imported content through 5e.tools.

## Repository Structure

```text
wm4-homebrew/
├── Components/          # Category-specific homebrew JSON data
├── Converter/           # Content conversion utilities and supporting data
├── Scripts/             # Catalog compilation and sorting scripts
├── auto-wm4-homebrew.json
├── wm4-homebrew.json    # Main catalog for 5e.tools
└── README.md
```

### Main Files

| File or directory | Purpose |
|---|---|
| `wm4-homebrew.json` | Compiled catalog intended for loading into 5e.tools |
| `auto-wm4-homebrew.json` | Additional compiled homebrew dataset maintained in the repository |
| `Components/` | Individual JSON files organized by homebrew category |
| `Scripts/compiler.py` | Combines component files into the main catalog JSON |
| `Scripts/sorter.py` | Sorts entries according to sorting rules defined in component metadata |
| `Converter/` | Contains utilities for converting structured reward text into homebrew data, along with supporting files |

## Maintaining the Catalog

The repository separates individual content categories into JSON files under `Components/`. These component files are combined to produce the main `wm4-homebrew.json` catalog.

The compilation utility reads the component data, combines entries by category, and updates the generated catalog metadata.

If you are contributing to the catalog, make changes to the relevant source data and regenerate the compiled JSON when appropriate. Review the generated output before committing changes.

**Note:** The conversion utilities include local file-path assumptions, so they may require configuration before running on another computer.

## Missing or Incorrect Content

The 5e.tools catalog is updated periodically as rewards are issued and added to the official homebrew catalog. As a result, there may be a delay between receiving a reward and seeing it in 5e.tools.

If a reward has been outstanding for more than a week:

1. Check the [Westmarch UTD Homebrew Catalog](https://docs.google.com/document/d/1tiToA5RnKt2pGXsPIT8XXOBbRKFVEKu-2gs7H3psY6I/edit?tab=t.0).
2. If the reward is missing from the catalog, contact the GM who issued it and ask them to add it.
3. If the reward is already listed in the catalog but is missing from 5e.tools, send a direct message to the maintainer or mention them in the `#wm-discussion` channel.

This helps distinguish missing source content from content that has not yet been incorporated into the searchable dataset.

## Updates and Notifications

To stay informed about catalog changes, enable notifications for the associated discussion thread. Updates should be announced when new content is added or existing content is updated.

## Credits

- **Content source:** Westmarch UTD, with contributions from its various Dungeon Masters.
- **Catalog and conversion tooling:** Maintained by contributors to this repository.
- **Search and browsing:** [5e.tools](https://5e.tools).

---

*Built to make Westmarch UTD's homebrew content easier to find, browse, and use.*
