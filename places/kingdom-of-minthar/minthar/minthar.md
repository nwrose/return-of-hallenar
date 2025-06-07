---
aliases:
- Minthar proper
- Minthar (city)
- City of Minthar
plane: '[[Planes/Overworld/Overworld|Overworld]]'
country: '[[Places/Kingdom of Minthar/Kingdom of Minthar|Kingdom of Minthar]]'
city: '[[Places/Kingdom of Minthar/Minthar/Minthar|Minthar]]'
district: null
locationAffiliations: null
factions:
- '[[Factions/Minthar Factions/Minthar Factions|Minthar Factions]]'
- '[[Factions/Minthar Factions/Council of Mages/Council of Mages|Council of Mages]]'
- '[[Factions/Minthar Factions/Expendable Family/Expendable Family|Expendable Family]]'
- '[[Factions/Minthar Factions/Minthar Central Government/Minthar Central Government|Minthar Central Government]]'
playerAffiliations: null
noteableNPCs:
- '[[NPCs/Vallencia NPCs/Vallencia Core NPCs/Sir Expendable/Sir Expendable|Sir Expendable]]'
- '[[NPCs/Minthar NPCs/Sir Expendable Sr/Sir Expendable Sr|Sir Expendable Sr]]'
- '[[NPCs/Minthar NPCs/King of Minthar/King of Minthar|King of Minthar]]'
- '[[NPCs/Minthar NPCs/Kaili Luvten/Kaili Luvten|Kaili Luvten]]'
- '[[NPCs/Vallence NPCs/Iron Veil NPCs/Ignis Luvten/Ignis Luvten|Ignis Luvten]]'
noteableItems: null
tags:
- place
---

# Minthar

**Tags:** `= this.file.tags`
Plane: `= this.plane`
Country: `= this.country`
**City**: `= this.city`
**District:** `= this.district`
**Factions:** `= this.factions`
**Player Affiliations:** `= this.playerAffiliations`
**Affiliated Locations:** `= this.locationAffiliations`

## Description

````dataviewjs
/**
 * Consolidated Hierarchy Items Template
 *
 * This template aggregates a specific property (e.g., 'keyMembers', 'secondaryLocations')
 * from the current file and all sub-files within the current file's folder hierarchy.
 *
 * It assumes:
 * - This script is placed in the 'top-level' file of your hierarchy (e.g., 'Thieves Guild/Thieves Guild.md').
 * - The property you want to aggregate is consistently named across all files.
 *
 * CUSTOMIZE THESE VARIABLES:
 * --------------------------
 * 1. `ITEM_PROPERTY_NAME`: The name of the property you want to collect (e.g., 'keyMembers', 'secondaryLocations').
 * 2. `COLLECTED_ITEM_NAME_PLURAL`: A descriptive name for the collected items (e.g., 'Key Members', 'Locations').
 * --------------------------
 */
const ITEM_PROPERTY_NAME = 'noteableNPCs'; // <--- CHANGE THIS to your property name (e.g., 'secondaryLocations')
const COLLECTED_ITEM_NAME_PLURAL = 'Noteable NPCs'; // <--- CHANGE THIS to your desired output label (e.g., 'Locations')

let allCollectedItems = [];

// Get the current file's object for its properties and path
const currentFile = dv.current();

// Determine the aggregation folder path: This is the folder of the current file.
const aggregationFolderPath = currentFile.file.folder;

// 1. Add items from the CURRENT main aggregation document
if (currentFile[ITEM_PROPERTY_NAME]) {
    if (Array.isArray(currentFile[ITEM_PROPERTY_NAME])) {
        allCollectedItems = allCollectedItems.concat(currentFile[ITEM_PROPERTY_NAME]);
    } else {
        // Handle if the property is a single string (not an array)
        allCollectedItems.push(currentFile[ITEM_PROPERTY_NAME]);
    }
}

// 2. Get all pages within the determined aggregation folder path and its subfolders.
//    We explicitly exclude the current file itself to prevent redundant processing.
let allRelevantPages = dv.pages(`"${aggregationFolderPath}"`)
                     .where(p => p.file.path !== currentFile.file.path);

// 3. Iterate through each discovered sub-page and collect their items.
for (let page of allRelevantPages) {
    if (page[ITEM_PROPERTY_NAME]) {
        if (Array.isArray(page[ITEM_PROPERTY_NAME])) {
            allCollectedItems = allCollectedItems.concat(page[ITEM_PROPERTY_NAME]);
        } else {
            allCollectedItems.push(page[ITEM_PROPERTY_NAME]);
        }
    }
}

// Remove any duplicates and sort the final list alphabetically
let uniqueAndSortedItems = [...new Set(allCollectedItems)].sort();

// Output the combined list as a paragraph or a markdown list
dv.paragraph(`## ${COLLECTED_ITEM_NAME_PLURAL} `)

if (uniqueAndSortedItems.length > 0) {
    dv.list(uniqueAndSortedItems)
} else {
    dv.list();
}

// If you prefer a markdown list instead, uncomment the line below:
// dv.list(uniqueAndSortedItems);
````

````dataviewjs
/**
 * Consolidated Hierarchy Items Template
 *
 * This template aggregates a specific property (e.g., 'keyMembers', 'secondaryLocations')
 * from the current file and all sub-files within the current file's folder hierarchy.
 *
 * It assumes:
 * - This script is placed in the 'top-level' file of your hierarchy (e.g., 'Thieves Guild/Thieves Guild.md').
 * - The property you want to aggregate is consistently named across all files.
 *
 * CUSTOMIZE THESE VARIABLES:
 * --------------------------
 * 1. `ITEM_PROPERTY_NAME`: The name of the property you want to collect (e.g., 'keyMembers', 'secondaryLocations').
 * 2. `COLLECTED_ITEM_NAME_PLURAL`: A descriptive name for the collected items (e.g., 'Key Members', 'Locations').
 * --------------------------
 */
const ITEM_PROPERTY_NAME = 'noteableItems'; // <--- CHANGE THIS to your property name (e.g., 'secondaryLocations')
const COLLECTED_ITEM_NAME_PLURAL = 'Noteable Items'; // <--- CHANGE THIS to your desired output label (e.g., 'Locations')

let allCollectedItems = [];

// Get the current file's object for its properties and path
const currentFile = dv.current();

// Determine the aggregation folder path: This is the folder of the current file.
const aggregationFolderPath = currentFile.file.folder;

// 1. Add items from the CURRENT main aggregation document
if (currentFile[ITEM_PROPERTY_NAME]) {
    if (Array.isArray(currentFile[ITEM_PROPERTY_NAME])) {
        allCollectedItems = allCollectedItems.concat(currentFile[ITEM_PROPERTY_NAME]);
    } else {
        // Handle if the property is a single string (not an array)
        allCollectedItems.push(currentFile[ITEM_PROPERTY_NAME]);
    }
}

// 2. Get all pages within the determined aggregation folder path and its subfolders.
//    We explicitly exclude the current file itself to prevent redundant processing.
let allRelevantPages = dv.pages(`"${aggregationFolderPath}"`)
                     .where(p => p.file.path !== currentFile.file.path);

// 3. Iterate through each discovered sub-page and collect their items.
for (let page of allRelevantPages) {
    if (page[ITEM_PROPERTY_NAME]) {
        if (Array.isArray(page[ITEM_PROPERTY_NAME])) {
            allCollectedItems = allCollectedItems.concat(page[ITEM_PROPERTY_NAME]);
        } else {
            allCollectedItems.push(page[ITEM_PROPERTY_NAME]);
        }
    }
}

// Remove any duplicates and sort the final list alphabetically
let uniqueAndSortedItems = [...new Set(allCollectedItems)].sort();

dv.paragraph(`## ${COLLECTED_ITEM_NAME_PLURAL} `)

if (uniqueAndSortedItems.length > 0) {
    dv.list(uniqueAndSortedItems)
} else {
    dv.list();
}

// If you prefer a markdown list instead, uncomment the line below:
// dv.list(uniqueAndSortedItems);
````
