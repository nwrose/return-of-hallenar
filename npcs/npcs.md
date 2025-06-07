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

* [Balken Ribb](npcs/vallencia-npcs/vallencia-core-npcs/balken-ribb/balken-ribb.md)
* [Cassian Veylin](npcs/vallence-npcs/iron-veil-npcs/cassian-veylin/cassian-veylin.md)
* [Culvis](npcs/vallencia-npcs/vallencia-core-npcs/culvis/culvis.md)
* [Deities](npcs/deities/deities.md)
* [DJ Aetheris](npcs/vallence-npcs/iron-veil-npcs/dj-aetheris/dj-aetheris.md)
* [Doctor Lucious White](npcs/vallence-npcs/ebon-quill-npcs/doctor-lucious-white/doctor-lucious-white.md)
* [Dracus Sinthar](npcs/vallencia-npcs/vallencia-parliament-npcs/dracus-sinthar/dracus-sinthar.md)
* [Ebon Quill NPCs](npcs/vallence-npcs/ebon-quill-npcs/ebon-quill-npcs.md)
* [Elise](npcs/vallencia-npcs/vallencia-core-npcs/elise/elise.md)
* [Fake Chariel](npcs/vallencia-npcs/vallencia-core-npcs/fake-chariel/fake-chariel.md)
* [Frank (Iron Veil)](../NPCs/Vallence%20NPCs/Iron%20Veil%20NPCs/Frank%20(Iron%20Veil)/Frank%20(Iron%20Veil).md)
* [Frog Elder](npcs/vallencia-npcs/vallencia-core-npcs/frog-elder/frog-elder.md)
* [Front Desk Twins (Doormen)](../NPCs/Vallencia%20NPCs/Misc%20Vallencia%20NPCs/Front%20Desk%20Twins%20(Doormen)/Front%20Desk%20Twins%20(Doormen).md)
* [Garruk Ironstitch](npcs/vallence-npcs/vallence-core-npcs/garruk-ironstitch/garruk-ironstitch.md)
* [Guzzlethroat the Magnificent](npcs/vallencia-npcs/vallencia-core-npcs/guzzlethroat-the-magnificent/guzzlethroat-the-magnificent.md)
* [Ignis Luvten](npcs/vallence-npcs/iron-veil-npcs/ignis-luvten/ignis-luvten.md)
* [Ignis' Boi](npcs/vallence-npcs/iron-veil-npcs/ignis-boi/ignis-boi.md)
* [Iron Mask](npcs/vallence-npcs/iron-veil-npcs/iron-mask/iron-mask.md)
* [Iron Veil NPCs](npcs/vallence-npcs/iron-veil-npcs/iron-veil-npcs.md)
* [Jex](npcs/vallence-npcs/iron-veil-npcs/jex/jex.md)
* [Kaili Luvten](npcs/minthar-npcs/kaili-luvten/kaili-luvten.md)
* [Kathilda Stallia](npcs/vallencia-npcs/vallencia-core-npcs/kathilda-stallia/kathilda-stallia.md)
* [King of Minthar](npcs/minthar-npcs/king-of-minthar/king-of-minthar.md)
* [Lina Kaldros](npcs/vallence-npcs/iron-veil-npcs/lina-kaldros/lina-kaldros.md)
* [Malrik](npcs/vallence-npcs/ebon-quill-npcs/malrik/malrik.md)
* [Man coerced by Fake Chariel](npcs/vallencia-npcs/misc-vallencia-npcs/man-coerced-by-fake-chariel/man-coerced-by-fake-chariel.md)
* [Minthar NPCs](npcs/minthar-npcs/minthar-npcs.md)
* [Misc Vallence NPCs](npcs/vallence-npcs/misc-vallence-npcs/misc-vallence-npcs.md)
* [Misc Vallencia NPCs](npcs/vallencia-npcs/misc-vallencia-npcs/misc-vallencia-npcs.md)
* [Monsters](npcs/monsters/monsters.md)
* [Mysterious Note Writer](npcs/vallence-npcs/vallence-core-npcs/mysterious-note-writer/mysterious-note-writer.md)
* [Nicholas Sutter](npcs/vallencia-npcs/vallencia-parliament-npcs/nicholas-sutter/nicholas-sutter.md)
* [Parliament Guards](npcs/vallencia-npcs/vallencia-parliament-npcs/parliament-guards/parliament-guards.md)
* [Penny](npcs/vallence-npcs/misc-vallence-npcs/penny/penny.md)
* [Piercing Pen Clerk](npcs/vallence-npcs/misc-vallence-npcs/piercing-pen-clerk/piercing-pen-clerk.md)
* [Potions Lady](npcs/vallence-npcs/vallence-core-npcs/potions-lady/potions-lady.md)
* [Rutha](npcs/vallence-npcs/iron-veil-npcs/rutha/rutha.md)
* [Selena](npcs/vallencia-npcs/vallencia-parliament-npcs/selena/selena.md)
* [Selene Veyne](npcs/vallence-npcs/ebon-quill-npcs/selene-veyne/selene-veyne.md)
* [Seraphim Vos](npcs/vallence-npcs/iron-veil-npcs/seraphim-vos/seraphim-vos.md)
* [Shartrice](npcs/vallence-npcs/misc-vallence-npcs/shartrice/shartrice.md)
* [Sherman Corn](npcs/vallencia-npcs/vallencia-core-npcs/sherman-corn/sherman-corn.md)
* [Shirley Topplepots](npcs/vallencia-npcs/misc-vallencia-npcs/shirley-topplepots/shirley-topplepots.md)
* [Sicily Quickstep](npcs/vallencia-npcs/vallencia-core-npcs/sicily-quickstep/sicily-quickstep.md)
* [Simon](npcs/vallencia-npcs/misc-vallencia-npcs/simon/simon.md)
* [Sir Expendable](npcs/vallencia-npcs/vallencia-core-npcs/sir-expendable/sir-expendable.md)
* [Sir Expendable Sr](npcs/minthar-npcs/sir-expendable-sr/sir-expendable-sr.md)
* [Suzie](npcs/vallence-npcs/iron-veil-npcs/suzie/suzie.md)
* [Thad Quadra](npcs/vallencia-npcs/misc-vallencia-npcs/thad-quadra/thad-quadra.md)
* [Tim](npcs/vallencia-npcs/vallencia-core-npcs/tim/tim.md)
* [Timothee the Chalamet](npcs/vallencia-npcs/misc-vallencia-npcs/timothee-the-chalamet/timothee-the-chalamet.md)
* [Vallence Core NPCs](npcs/vallence-npcs/vallence-core-npcs/vallence-core-npcs.md)
* [Vallence NPCs](npcs/vallence-npcs/vallence-npcs.md)
* [Vallencia Core NPCs](npcs/vallencia-npcs/vallencia-core-npcs/vallencia-core-npcs.md)
* [Vallencia NPCs](npcs/vallencia-npcs/vallencia-npcs.md)
* [Vallencia Parliament NPCs](npcs/vallencia-npcs/vallencia-parliament-npcs/vallencia-parliament-npcs.md)
* [Vallencia's Legendary Heroes](npcs/vallencia-npcs/vallencias-legendary-heroes/vallencias-legendary-heroes.md)
* [WW&W Shopkeep Boy](npcs/vallencia-npcs/misc-vallencia-npcs/wwandw-shopkeep-boy/wwandw-shopkeep-boy.md)
