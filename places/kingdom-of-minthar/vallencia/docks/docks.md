---
aliases:
- Vallencia Port
plane: '"Overworld"'
country: '"Kingdom of Minthar"'
city: '"Vallencia"'
district: '"Vallencia Lower Ring"'
locationAffiliations:
- '"Juju Island"'
- '"Vallence"'
- '"The Salty Barnacle"'
- '"Stallia Shipping Company HQ"'
- '"Stallia Shipping Company Warehouse"'
playerAffiliations:
- '"Chariel Von Dutch"'
factions:
- '"Stallia Shipping Company"'
- '"Cult of Hallenar"'
noteableNPCs: null
noteableItems:
- '"Note with earthquake schedule"'
tags:
- place
- docks
- port
- lower
- ring
- east
---

# The Docks of Vallencia

**Tags:** `= this.file.tags`
Plane: `= this.plane`
Country: `= this.country`
**City**: `= this.city`
**District:** `= this.district`
**Factions:** `= this.factions`
**Player Affiliations:** `= this.playerAffiliations`
**Affiliated Locations:** `= this.locationAffiliations`

## Description

Even before the sun dares to fully breach the horizon, painting the vast eastern ocean with nascent fire, the Docks of Vallencia are alive. A symphony of creaking wood, the mournful cries of early gulls, and the rhythmic crash of tides against the stone quays forms the city’s morning hymn. Here, where the great rivers of Vallencia meet the sea and begin their journey inland as watery streets, dockworkers, their brows already slick with sweat, move with a life-forged resolve. Captains, emerging from a long night at the infamous Salty Barnacle, bark orders, their voices rough with ale and lack of sleep.

Yet, an unseasonal chill clings to the air, a palpable dread that has little to do with the morning mist. Sailors murmur anxiously of the recent turmoil on the waters, waves lashing with a fury unseen in living memory, prompting desperate pleas for captains to consult fortunetellers before casting off. The usual dockside banter—tales of brawls at the Barnacle, gossip of a boss's wayward child, or the unsettling whispers of friends who ventured down into the shadowy depths of Vallence via the known access points, never to return, and even hushed mentions of missing children—is now tinged with a deeper fear. Far across the turbulent waves, one can barely perceive the silhouette of Juju Island, Vallencia's partner in the lucrative fruit trade, its shores seeming to recede into elongated, ominous shadows. The "Rumblings" often associated with this area only add to the unease, hinting at the Cult's shadowy influence.

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
