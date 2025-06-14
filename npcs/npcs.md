---
sticker: emoji//1f46d
group_tag:
- NPCs
---

# All NPCs

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
					fileName === folderName
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

* [Balken Ribb](/npcs/vallencia-npcs/vallencia-core-npcs/balken-ribb/balken-ribb)
* [Cassian Veylin](/npcs/vallence-npcs/iron-veil-npcs/cassian-veylin/cassian-veylin)
* [Culvis](/npcs/vallencia-npcs/vallencia-core-npcs/culvis/culvis)
* [Deities](/npcs/deities/deities)
* [DJ Aetheris](/npcs/vallence-npcs/iron-veil-npcs/dj-aetheris/dj-aetheris)
* [Doctor Lucious White](/npcs/vallence-npcs/ebon-quill-npcs/doctor-lucious-white/doctor-lucious-white)
* [Dracus Sinthar](/npcs/vallencia-npcs/vallencia-parliament-npcs/dracus-sinthar/dracus-sinthar)
* [Ebon Quill NPCs](/npcs/vallence-npcs/ebon-quill-npcs/ebon-quill-npcs)
* [Elise](/npcs/vallencia-npcs/vallencia-core-npcs/elise/elise)
* [Fake Chariel](/npcs/vallencia-npcs/vallencia-core-npcs/fake-chariel/fake-chariel)
* [Frank (Iron Veil)](../NPCs/Vallence%20NPCs/Iron%20Veil%20NPCs/Frank%20(Iron%20Veil)/Frank%20(Iron%20Veil).md)
* [Frog Elder](/npcs/vallencia-npcs/vallencia-core-npcs/frog-elder/frog-elder)
* [Front Desk Twins (Doormen)](../NPCs/Vallencia%20NPCs/Misc%20Vallencia%20NPCs/Front%20Desk%20Twins%20(Doormen)/Front%20Desk%20Twins%20(Doormen).md)
* [Garruk Ironstitch](/npcs/vallence-npcs/vallence-core-npcs/garruk-ironstitch/garruk-ironstitch)
* [Guzzlethroat the Magnificent](/npcs/vallencia-npcs/vallencia-core-npcs/guzzlethroat-the-magnificent/guzzlethroat-the-magnificent)
* [Ignis Luvten](/npcs/vallence-npcs/iron-veil-npcs/ignis-luvten/ignis-luvten)
* [Ignis' Boi](/npcs/vallence-npcs/iron-veil-npcs/ignis-boi/ignis-boi)
* [Iron Mask](/npcs/vallence-npcs/iron-veil-npcs/iron-mask/iron-mask)
* [Iron Veil NPCs](/npcs/vallence-npcs/iron-veil-npcs/iron-veil-npcs)
* [Jex](/npcs/vallence-npcs/iron-veil-npcs/jex/jex)
* [Kaili Luvten](/npcs/minthar-npcs/kaili-luvten/kaili-luvten)
* [Kathilda Stallia](/npcs/vallencia-npcs/vallencia-core-npcs/kathilda-stallia/kathilda-stallia)
* [King of Minthar](/npcs/minthar-npcs/king-of-minthar/king-of-minthar)
* [Lina Kaldros](/npcs/vallence-npcs/iron-veil-npcs/lina-kaldros/lina-kaldros)
* [Malrik](/npcs/vallence-npcs/ebon-quill-npcs/malrik/malrik)
* [Man coerced by Fake Chariel](/npcs/vallencia-npcs/misc-vallencia-npcs/man-coerced-by-fake-chariel/man-coerced-by-fake-chariel)
* [Minthar NPCs](/npcs/minthar-npcs/minthar-npcs)
* [Misc Vallence NPCs](/npcs/vallence-npcs/misc-vallence-npcs/misc-vallence-npcs)
* [Misc Vallencia NPCs](/npcs/vallencia-npcs/misc-vallencia-npcs/misc-vallencia-npcs)
* [Monsters](/npcs/monsters/monsters)
* [Mysterious Note Writer](/npcs/vallence-npcs/vallence-core-npcs/mysterious-note-writer/mysterious-note-writer)
* [Nicholas Sutter](/npcs/vallencia-npcs/vallencia-parliament-npcs/nicholas-sutter/nicholas-sutter)
* [Parliament Guards](/npcs/vallencia-npcs/vallencia-parliament-npcs/parliament-guards/parliament-guards)
* [Penny](/npcs/vallence-npcs/misc-vallence-npcs/penny/penny)
* [Piercing Pen Clerk](/npcs/vallence-npcs/misc-vallence-npcs/piercing-pen-clerk/piercing-pen-clerk)
* [Potions Lady](/npcs/vallence-npcs/vallence-core-npcs/potions-lady/potions-lady)
* [Rutha](/npcs/vallence-npcs/iron-veil-npcs/rutha/rutha)
* [Selena](/npcs/vallencia-npcs/vallencia-parliament-npcs/selena/selena)
* [Selene Veyne](/npcs/vallence-npcs/ebon-quill-npcs/selene-veyne/selene-veyne)
* [Seraphim Vos](/npcs/vallence-npcs/iron-veil-npcs/seraphim-vos/seraphim-vos)
* [Shartrice](/npcs/vallence-npcs/misc-vallence-npcs/shartrice/shartrice)
* [Sherman Corn](/npcs/vallencia-npcs/vallencia-core-npcs/sherman-corn/sherman-corn)
* [Shirley Topplepots](/npcs/vallencia-npcs/misc-vallencia-npcs/shirley-topplepots/shirley-topplepots)
* [Sicily Quickstep](/npcs/vallencia-npcs/vallencia-core-npcs/sicily-quickstep/sicily-quickstep)
* [Simon](/npcs/vallencia-npcs/misc-vallencia-npcs/simon/simon)
* [Sir Expendable](/npcs/vallencia-npcs/vallencia-core-npcs/sir-expendable/sir-expendable)
* [Sir Expendable Sr](/npcs/minthar-npcs/sir-expendable-sr/sir-expendable-sr)
* [Suzie](/npcs/vallence-npcs/iron-veil-npcs/suzie/suzie)
* [Thad Quadra](/npcs/vallencia-npcs/misc-vallencia-npcs/thad-quadra/thad-quadra)
* [Tim](/npcs/vallencia-npcs/vallencia-core-npcs/tim/tim)
* [Timothee the Chalamet](/npcs/vallencia-npcs/misc-vallencia-npcs/timothee-the-chalamet/timothee-the-chalamet)
* [Vallence Core NPCs](/npcs/vallence-npcs/vallence-core-npcs/vallence-core-npcs)
* [Vallence NPCs](/npcs/vallence-npcs/vallence-npcs)
* [Vallencia Core NPCs](/npcs/vallencia-npcs/vallencia-core-npcs/vallencia-core-npcs)
* [Vallencia NPCs](/npcs/vallencia-npcs/vallencia-npcs)
* [Vallencia Parliament NPCs](/npcs/vallencia-npcs/vallencia-parliament-npcs/vallencia-parliament-npcs)
* [Vallencia's Legendary Heroes](/npcs/vallencia-npcs/vallencias-legendary-heroes/vallencias-legendary-heroes)
* [WW&W Shopkeep Boy](/npcs/vallencia-npcs/misc-vallencia-npcs/wwandw-shopkeep-boy/wwandw-shopkeep-boy)
