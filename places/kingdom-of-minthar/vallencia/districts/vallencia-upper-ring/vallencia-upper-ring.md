---
aliases: []
plane: '[[Planes/Overworld/Overworld|Overworld]]'
country: '[[Places/Kingdom of Minthar/Kingdom of Minthar|Kingdom of Minthar]]'
city: '[[Places/Kingdom of Minthar/Vallencia/Vallencia|Vallencia]]'
district: '[[Places/Kingdom of Minthar/Vallencia/Districts/Vallencia Upper Ring/Vallencia Upper Ring|Vallencia Upper Ring]]'
locationAffiliations:
- '[[Places/Kingdom of Minthar/Vallencia/Vallencia Parliament Building/Vallencia Parliament Building|Vallencia Parliament Building]]'
- '[[Places/Kingdom of Minthar/Vallencia/Vallencia Parliament Treasury/Vallencia Parliament Treasury|Vallencia Parliament Treasury]]'
- '[[Places/Kingdom of Minthar/Vallencia/Guzzlethroat''s Penthouse/Guzzlethroat''s Penthouse|Guzzlethroat''s Penthouse]]'
- '[[Places/Kingdom of Minthar/Vallencia/Districts/Vallencia Upper Ring/Von Dutch Estate/Von Dutch Estate|Von Dutch Estate]]'
playerAffiliations:
- '[[Players/Chariel Von Dutch/Chariel Von Dutch|Chariel Von Dutch]]'
factions:
- '[[Factions/Vallencia Factions/Vallencia Parliament/Vallencia Parliament|Vallencia Parliament]]'
- '[[Factions/Vallencia Factions/Stallia Shipping Company/Stallia Shipping Company|Stallia Shipping Company]]'
noteableNPCs:
- '[[NPCs/Vallencia NPCs/Vallencia Core NPCs/Guzzlethroat the Magnificent/Guzzlethroat the Magnificent|Guzzlethroat the Magnificent]]'
- '[[NPCs/Vallencia NPCs/Vallencia Parliament NPCs/Dracus Sinthar/Dracus Sinthar|Dracus Sinthar]]'
- '[[NPCs/Vallencia NPCs/Vallencia Parliament NPCs/Nicholas Sutter/Nicholas Sutter|Nicholas Sutter]]'
- '[[NPCs/Vallencia NPCs/Vallencia Parliament NPCs/Selena/Selena|Selena]]'
- '[[NPCs/Vallencia NPCs/Vallencia Core NPCs/Kathilda Stallia/Kathilda Stallia|Kathilda Stallia]]'
- '[[NPCs/Vallencia NPCs/Vallencia Core NPCs/Culvis/Culvis|Culvis]]'
noteableItems: null
tags:
- place
- district
- upper
- ring
- elite
- political
- residential
- opulent
---

# The Upper Ring of Vallencia

**Tags:** `= this.file.tags`
Plane: `= this.plane`
Country: `= this.country`
**City**: `= this.city`
**District:** `= this.district`
**Factions:** `= this.factions`
**Player Affiliations:** `= this.playerAffiliations`
**Affiliated Locations:** `= this.locationAffiliations`

## Description

At Vallencia's zenith lies the Upper Ring, a realm of breathtaking beauty and rarefied air, where the city's river-streets are transformed into gracefully managed, crystal-clear canals, reflecting the opulent marble and manicured gardens that line their banks. Sunlight here is "glorious," bathing the "extravagant homes" of nobles and the pristine facades of power in a golden glow. The Von Dutch estate, for instance, stands as a testament to generational wealth, its walls perhaps overlooking these serene waterways. The grand Vallencia Parliament building, where the city's laws and regulations are crafted, is a focal point of this district, its architecture imposing and authoritative.

This is the domain of Vallencia's elite, who rarely descend for their needs, preferring to dispatch servants in well-appointed boats to the markets below. Any commercial establishments here are exceedingly "extravagant," catering exclusively to the "highest esteemed people." The streets and plazas are cleaner, the atmosphere more serene, if a touch aloof. It is here one finds the magnificent Vallencia Players Theatre, where grand productions unfold, and perched at the very apex of the city, Guzzlethroat's Penthouse, offering unparalleled views. To the east, the ocean glitters invitingly; to the west, the vast plains of the Kingdom of Minthar stretch towards a distant horizon, where one might almost imagine the capital city itself. Music of a more refined nature can often be heard from private balconies or exclusive establishments, and it is here, during events like the [Centennial Sealing Festival](/plotlines/history-of-vallencia/centennial-sealing-festival), that tales of [Vallencia's Legendary Heroes](/npcs/vallencia-npcs/vallencias-legendary-heroes/vallencias-legendary-heroes) are recounted with particular pomp.

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
