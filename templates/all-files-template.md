---
group_tag: []
---

# All {{title}} (A-Z)

````dataviewjs
if (true) {
	const currentDepth = dv.current().file.path.split("/").length - 1;
	const currentFolder = dv.current().file.folder;
	
	const pages = dv.pages()
		.where(p => p.file.folder.startsWith(currentFolder))
		.sort(p => p.file.name);
	
	dv.list(pages.map(p => {
		const upward = '../'.repeat(currentDepth);
		const relPath = upward + encodeURI(p.file.path);
		return `\\[${p.file.name}](${relPath})`;
	}));
} else {
	dv.paragraph("Refresh");
}
````
