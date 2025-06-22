---
aliases:
- The Cult
- CoH
- Cult of Hallenar
Leader: null
keyMembers:
- '"NPCs/Vallence NPCs/Iron Veil NPCs/Seraphim Vos"'
factionSize: Large
primaryLocation: null
secondaryLocations: null
branches: null
playerAttitude: Hostile
noteableItems:
- '"Cult Pin"'
- '"Poisoned Juju Fruit"'
- '"Hallenar''s Sealing Journal"'
- '"Key to Hallenar''s Sealing Journal"'
- '"Note with earthquake schedule"'
tags:
- Faction
---

# The Cult of Hallenar

**Tags:** `= this.file.tags`
**Leader:** `= this.leader`
**Faction Size:** `= this.factionSize`
**Primary Location:** `= this.primaryLocation`

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
const ITEM_PROPERTY_NAME = 'secondaryLocations'; // <--- CHANGE THIS to your property name (e.g., 'secondaryLocations')
const COLLECTED_ITEM_NAME_PLURAL = 'Other Locations'; // <--- CHANGE THIS to your desired output label (e.g., 'Locations')

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
if (uniqueAndSortedItems.length > 0) {
    dv.paragraph(`**${COLLECTED_ITEM_NAME_PLURAL}: **` + uniqueAndSortedItems.join(", "));
} else {
    dv.paragraph(`**${COLLECTED_ITEM_NAME_PLURAL}: **None`);
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
const ITEM_PROPERTY_NAME = 'keyMembers'; // <--- CHANGE THIS to your property name (e.g., 'secondaryLocations')
const COLLECTED_ITEM_NAME_PLURAL = 'Key Members'; // <--- CHANGE THIS to your desired output label (e.g., 'Locations')

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
let uniqueAndSortedItems = [...new Set(allCollectedItems)];

// Output the combined list as a paragraph or a markdown list
if (uniqueAndSortedItems.length > 0) {
    dv.paragraph(`**${COLLECTED_ITEM_NAME_PLURAL}: **` + uniqueAndSortedItems.join(", "));
} else {
    dv.paragraph(`**${COLLECTED_ITEM_NAME_PLURAL}: **None`);
}

// If you prefer a markdown list instead, uncomment the line below:
// dv.list(uniqueAndSortedItems);
````

**Player Attitude:** `= this.playerAttitude`

## Description

The Cult of Hallenar is an apocalyptic cult bent on returning the deity [Hallenar](/factions/the-cult-of-hallenar/hallenar) that laid waste to the [Kingdom of Minthar](/places/kingdom-of-minthar/kingdom-of-minthar) 2000 years ago and plunge the world into chaos and destruction so that a new world can come about. The cult has a following that spans the Kingdom of Minthar. Cult members are seldom seen in public, with the exception of highly involved zealots. Beginning as a religious rebellion against the Mintharian government, the cult has recruited membership from various demographics since its inception, with impoverished, neglected, and/or persecuted communities being especially receptive to their message of "a reset of society."

## Background

## Values

The cult values are based upheaving [The Seven Sins of Civilization](/factions/the-cult-of-hallenar/the-seven-sins-of-civilization/the-seven-sins-of-civilization). Those being:

1. [Gluttony](/factions/the-cult-of-hallenar/the-seven-sins-of-civilization/gluttony) – The Overconsumption of Nature
1. [Destruction](/factions/the-cult-of-hallenar/the-seven-sins-of-civilization/destruction) – The Devastation of Natural Land
1. [Order](/factions/the-cult-of-hallenar/the-seven-sins-of-civilization/order) – The Lie of Civilization’s Stability
1. [Hubris](/factions/the-cult-of-hallenar/the-seven-sins-of-civilization/hubris) – The Illusion of Human Supremacy
1. [Ignorance & Indifference](/factions/the-cult-of-hallenar/the-seven-sins-of-civilization/ignorance-and-indifference) – The Blind and the Uncaring
1. [Mortality](/factions/the-cult-of-hallenar/the-seven-sins-of-civilization/mortality) – The Fear of Death
1. 

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

// Output the combined list as a paragraph or a markdown list
dv.paragraph(`## ${COLLECTED_ITEM_NAME_PLURAL}: `)

if (uniqueAndSortedItems.length > 0) {
    dv.list(uniqueAndSortedItems)
} else {
    dv.list();
}

// If you prefer a markdown list instead, uncomment the line below:
// dv.list(uniqueAndSortedItems);
````
