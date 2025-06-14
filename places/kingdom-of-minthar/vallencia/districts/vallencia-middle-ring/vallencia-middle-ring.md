---
aliases:
- The Merchant Ring
plane: '[[Planes/Overworld/Overworld|Overworld]]'
country: '[[Places/Kingdom of Minthar/Kingdom of Minthar|Kingdom of Minthar]]'
city: '[[Places/Kingdom of Minthar/Vallencia/Vallencia|Vallencia]]'
district: '[[Places/Kingdom of Minthar/Vallencia/Districts/Vallencia Middle Ring/Vallencia Middle Ring|Vallencia Middle Ring]]'
locationAffiliations:
- '[[Places/Kingdom of Minthar/Vallencia/Vallencia Town Square/Vallencia Town Square|Vallencia Town Square]]'
- '[[Places/Kingdom of Minthar/Vallencia/The Not So Shabby Cat Inn/The Not So Shabby Cat Inn|The Not So Shabby Cat Inn]]'
- '[[Items/Shops/The Whimsy Wardrobe & Wares|The Whimsy Wardrobe & Wares]]'
- '[[Places/Kingdom of Minthar/Vallencia/Districts/Vallencia Entertainment District/Vallencia Entertainment District|Vallencia Entertainment District]]'
playerAffiliations: null
factions:
- '[[Factions/Vallencia Small Business Owner''s Association/Vallencia Small Business Owner''s Association|Vallencia Small Business Owner''s Association]]'
- '[[Factions/Vallencia Factions/Vallencia Amateur Theatre Troupe/Vallencia Amateur Theatre Troupe|Vallencia Amateur Theatre Troupe]]'
noteableNPCs:
- '[[NPCs/Vallencia NPCs/Vallencia Core NPCs/Balken Ribb/Balken Ribb|Balken Ribb]]'
noteableItems:
- '[[Items/Miscellaneous Items/Juju Fruit Pie|Juju Fruit Pie]]'
tags:
- place
- district
- middle
- ring
- market
- commercial
- residential
---

# The Middle Ring of Vallencia

**Tags:** `= this.file.tags`
Plane: `= this.plane`
Country: `= this.country`
**City**: `= this.city`
**District:** `= this.district`
**Factions:** `= this.factions`
**Player Affiliations:** `= this.playerAffiliations`
**Affiliated Locations:** `= this.locationAffiliations`

## Description

The Middle Ring is a vibrant artery of Vallencian life, where the man-made rivers that serve as streets flow more freely, reflecting a brighter sky than the Lower Ring. The hustle and bustle are invigorating; boats and gondolas navigate these watery avenues, alongside walkways crowded with people. Shops, built with colourful awnings and open fronts facing the canals and plazas, overflow with goods – from practical wares to vibrant clothing stitched in the Lower Ring, destined for the city's more affluent. Knick-knacks, exotic tchotchkes, bustling grocery stores, and sprawling markets create a tapestry of commerce. Children's laughter echoes as they play along the riverbanks and in the squares, and people generally look healthier and cleaner, though there's a wide variety of folk.

The Eastern Middle Ring, nearest the Docks, boasts the grand Vallencia Town Square, a place of public gathering and celebration. Nearby, the beloved "Not So Shabby Cat Inn" is a beacon of warmth and cheer, its nightly lively performances drawing crowds who revel in affordable entertainment and the unique, sweet-and-spicy aroma of Juju fruit. Here, the fruit is king, transformed into pies of legendary status, pastries, jams, jellies, candies, and even savory meals, a testament to Vallencia's southern Juju Island connection. Music often drifts from local bars in this part of the ring, raising people's spirits with tales of heroes passed, especially during festive times like the Sealing Festival.

(For the Western Middle Ring, see the [Vallencia Entertainment District](/places/kingdom-of-minthar/vallencia/districts/vallencia-entertainment-district/vallencia-entertainment-district) entry.)

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
