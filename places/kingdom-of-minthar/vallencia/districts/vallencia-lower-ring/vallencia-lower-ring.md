---
aliases: null
plane: '[[Planes/Overworld/Overworld|Overworld]]'
country: '[[Places/Kingdom of Minthar/Kingdom of Minthar|Kingdom of Minthar]]'
city: '[[Places/Kingdom of Minthar/Vallencia/Vallencia|Vallencia]]'
district: '[[Places/Kingdom of Minthar/Vallencia/Districts/Vallencia Lower Ring/Vallencia Lower Ring|Vallencia Lower Ring]]'
locationAffiliations:
- '[[Places/Kingdom of Minthar/Vallencia/Docks/Docks|Docks]]'
playerAffiliations: null
factions:
- '[[Factions/The Cult of Hallenar/The Cult of Hallenar|Cult of Hallenar]]'
noteableNPCs: null
noteableItems: null
tags:
- place
- district
- lower
- ring
- poverty
- residential
---

# The Lower Ring of Vallencia

**Tags:** `= this.file.tags`
Plane: `= this.plane`
Country: `= this.country`
**City**: `= this.city`
**District:** `= this.district`
**Factions:** `= this.factions`
**Player Affiliations:** `= this.playerAffiliations`
**Affiliated Locations:** `= this.locationAffiliations`

## Description

The Lower Ring is where the great rivers of Vallencia, serving as its streets, become more like murky, shadowed canals, squeezed between towering, densely packed townhomes that lean against each other as if for grim support. Sunlight is a reluctant visitor, choked out by the oppressive architecture, leaving the narrow watery streets and cramped alleyways in perpetual twilight. This is the realm of immigrants, souls from offshore kingdoms who sought a new beginning in Vallencia but found themselves mired in its underbelly.

The air is thick with the scent of hardship, damp stone, and refuse-choked water. The people, often demi-human or of less favored humanoid races, bear the grime of ceaseless labor in the textile factories or upon the nearby docks. Cleanliness is a forgotten luxury, appearances a burden they cannot afford. It is in this crucible of poverty, discrimination, and stifled ambition that the insidious whispers of the Cult of Hallenar find fertile ground. The Cult’s promises of an upheaval, a world reset where the downtrodden might start fresh, bloom like a patch of phosphorescent fungi in the darkness—a dangerous, intoxicating hope. Many here live a double life, their days filled with toil, their hearts secretly clinging to the prophecy of Hallenar's return, believing their suffering is but a prelude to a new dawn, however terrible the cost of its arrival.

````dataviewjs
/**
 * Consolidated Hierarchy Items Template
 */
const ITEM_PROPERTY_NAME = 'noteableNPCs';
const COLLECTED_ITEM_NAME_PLURAL = 'Noteable NPCs';
let allCollectedItems = [];
const currentFile = dv.current();
const aggregationFolderPath = currentFile.file.folder;
if (currentFile[ITEM_PROPERTY_NAME]) {
    if (Array.isArray(currentFile[ITEM_PROPERTY_NAME])) {
        allCollectedItems = allCollectedItems.concat(currentFile[ITEM_PROPERTY_NAME]);
    } else {
        allCollectedItems.push(currentFile[ITEM_PROPERTY_NAME]);
    }
}
let allRelevantPages = dv.pages(`"${aggregationFolderPath}"`)
                     .where(p => p.file.path !== currentFile.file.path);
for (let page of allRelevantPages) {
    if (page[ITEM_PROPERTY_NAME]) {
        if (Array.isArray(page[ITEM_PROPERTY_NAME])) {
            allCollectedItems = allCollectedItems.concat(page[ITEM_PROPERTY_NAME]);
        } else {
            allCollectedItems.push(page[ITEM_PROPERTY_NAME]);
        }
    }
}
let uniqueAndSortedItems = [...new Set(allCollectedItems)].sort();
dv.paragraph(`## ${COLLECTED_ITEM_NAME_PLURAL} `)
if (uniqueAndSortedItems.length > 0) {
    dv.list(uniqueAndSortedItems)
} else {
    dv.list();
}
````

````dataviewjs
/**
 * Consolidated Hierarchy Items Template
 */
const ITEM_PROPERTY_NAME = 'noteableItems';
const COLLECTED_ITEM_NAME_PLURAL = 'Noteable Items';
let allCollectedItems = [];
const currentFile = dv.current();
const aggregationFolderPath = currentFile.file.folder;
if (currentFile[ITEM_PROPERTY_NAME]) {
    if (Array.isArray(currentFile[ITEM_PROPERTY_NAME])) {
        allCollectedItems = allCollectedItems.concat(currentFile[ITEM_PROPERTY_NAME]);
    } else {
        allCollectedItems.push(currentFile[ITEM_PROPERTY_NAME]);
    }
}
let allRelevantPages = dv.pages(`"${aggregationFolderPath}"`)
                     .where(p => p.file.path !== currentFile.file.path);
for (let page of allRelevantPages) {
    if (page[ITEM_PROPERTY_NAME]) {
        if (Array.isArray(page[ITEM_PROPERTY_NAME])) {
            allCollectedItems = allCollectedItems.concat(page[ITEM_PROPERTY_NAME]);
        } else {
            allCollectedItems.push(page[ITEM_PROPERTY_NAME]);
        }
    }
}
let uniqueAndSortedItems = [...new Set(allCollectedItems)].sort();
dv.paragraph(`## ${COLLECTED_ITEM_NAME_PLURAL} `)
if (uniqueAndSortedItems.length > 0) {
    dv.list(uniqueAndSortedItems)
} else {
    dv.list();
}
````
