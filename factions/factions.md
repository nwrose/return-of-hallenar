---
sticker: emoji//1f9b9-200d-2640-fe0f
group_tag:
- Factions
---

# All Factions (A-Z)

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

* [Council of Mages](/factions/minthar-factions/council-of-mages/council-of-mages)
* [Expendable Family](/factions/minthar-factions/expendable-family/expendable-family)
* [Minthar Central Government](/factions/minthar-factions/minthar-central-government/minthar-central-government)
* [Minthar Factions](/factions/minthar-factions/minthar-factions)
* [Ragnar's Faction](/factions/ragnars-faction/ragnars-faction)
* [The Cult of Hallenar](/factions/the-cult-of-hallenar/the-cult-of-hallenar)
* [Thieves Guild](/factions/thieves-guild/thieves-guild)
* [Crimson Shroud](/factions/vallence-factions/crimson-shroud/crimson-shroud)
* [Ebon Quill](/factions/vallence-factions/ebon-quill/ebon-quill)
* [Iron Veil](/factions/vallence-factions/iron-veil/iron-veil)
* [Vallence Factions](/factions/vallence-factions/vallence-factions)
* [Guzzlethroat the Magnificent Fan Club](/factions/vallencia-factions/guzzlethroat-the-magnificent-fan-club/guzzlethroat-the-magnificent-fan-club)
* [Stallia Shipping Company](/factions/vallencia-factions/stallia-shipping-company/stallia-shipping-company)
* [Vallencia Amateur Theatre Troupe](/factions/vallencia-factions/vallencia-amateur-theatre-troupe/vallencia-amateur-theatre-troupe)
* [Vallencia Factions](/factions/vallencia-factions/vallencia-factions)
* [Vallencia Parliament](/factions/vallencia-factions/vallencia-parliament/vallencia-parliament)
* [Vallencia Players](/factions/vallencia-factions/vallencia-players/vallencia-players)
* [Vallencia Small Business Owner's Association](/factions/vallencia-small-business-owners-association/vallencia-small-business-owners-association)
