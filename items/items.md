---
sticker: emoji//2694-fe0f
group_tag:
- Items
---


````dataviewjs
if (false) {
	const currentDepth = dv.current().file.path.split("/").length - 1;
	let groupTags = dv.current().group_tag;

	if (!groupTags || groupTags.length==0) {
		dv.paragraph("⚠️ No 'group_tag' set in this file.");
	} else {
		// Normalize to array and lowercase all entries
		if (!Array.isArray(groupTags)) groupTags = [groupTags];
		groupTags = groupTags.map(t => t.toLowerCase());

		const pages = dv.pages()
			.where(p => {
				const pathParts = p.file.path.split("/");
				if (pathParts.length < 3) return false;

				const parentFolder = pathParts[pathParts.length - 3];
				const folderName = pathParts[pathParts.length - 2];
				const fileName = p.file.name;

				return (
					groupTags.some(tag => parentFolder.toLowerCase().includes(tag)) &&
					fileName !== folderName
				);
			})
			.sort(p => p.file.name);

		dv.list(pages.map(p => {
			const upward = '../'.repeat(currentDepth);
			const relPath = upward + encodeURI(p.file.path);
			return `\\[${p.file.name}](${relPath})`;
		}));
	}
} else {
	dv.paragraph("Refresh");
}
````

* [Amulet of Solario](/items/jewelry/amulet-of-solario)
* [Battle of Vallencia Memory Painting](/items/key-items/battle-of-vallencia-memory-painting)
* [Chariel's Dice](/items/key-items/chariels-dice)
* [Correspondence with Dracus Sinthar](/items/key-items/correspondence-with-dracus-sinthar)
* [Cult Pin](/items/key-items/cult-pin)
* [Ethereal Tuning Fork](/items/key-items/ethereal-tuning-fork)
* [Explosive Jelly](/items/weapons/explosive-jelly)
* [Green Juju Fruit](/items/key-items/green-juju-fruit)
* [Hallenar's Sealing Journal](/items/key-items/hallenars-sealing-journal)
* [Iron Veil Levitation Boots](/items/armor-and-clothing/iron-veil-levitation-boots)
* [Juju Fruit](/items/key-items/juju-fruit)
* [Juju Fruit Pie](/items/miscellaneous-items/juju-fruit-pie)
* [Key to Hallenar's Sealing Journal](/items/key-items/key-to-hallenars-sealing-journal)
* [Levitation Orb](/items/miscellaneous-items/levitation-orb)
* [Mask of Another](/items/armor-and-clothing/mask-of-another)
* [Note with earthquake schedule](/items/key-items/note-with-earthquake-schedule)
* [Poisoned Juju Fruit](/items/key-items/poisoned-juju-fruit)
* [Potion for Stiff Neck](/items/miscellaneous-items/potion-for-stiff-neck)
* [Rapier of Echos](/items/weapons/rapier-of-echos)
* [Seraphim's Research Log](/items/key-items/seraphims-research-log)
* [Song of Ages](/items/spells/song-of-ages)
* [The Whimsy Wardrobe & Wares](/items/shops/the-whimsy-wardrobe-and-wares)
* [Tim's Tracking spell](/items/spells/tims-tracking-spell)
* [Transmute Terrain](/items/spells/transmute-terrain)
