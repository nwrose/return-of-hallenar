---
sticker: emoji//1f4fd-fe0f
group_tag:
- Plotlines
---

# All Plotlines (A-Z)

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

* [History of Vallencia](/plotlines/history-of-vallencia/history-of-vallencia)
* [Revival of Hallenar](/plotlines/revival-of-hallenar/revival-of-hallenar)
* [Ragnar God of Chaos](/plotlines/ragnar-god-of-chaos/ragnar-god-of-chaos)
