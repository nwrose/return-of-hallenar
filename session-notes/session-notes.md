---
sticker: emoji//1f4da
group_tag:
- session notes
---


````dataviewjs
if (false) {
	const currentDepth = dv.current().file.path.split("/").length - 1;

const pages = dv.pages()
	.where(p => p.file.name.toLowerCase().includes("session"))
	.sort(p => p.file.name);

dv.list(pages.map(p => {
	const upward = '../'.repeat(currentDepth);
	const relPath = upward + encodeURI(p.file.path);
	return `\\[${p.file.name}](${relPath})`;  // Escaped \[ to prevent Obsidian auto-linking
}));
} else {
	dv.paragraph("Refresh");
}
````

* [Session 1🐸](../Session%20Notes/Session%201%F0%9F%90%B8.md)
* [Session 10🤵🏼‍♂️](../Session%20Notes/Session%2010%F0%9F%A4%B5%F0%9F%8F%BC%E2%80%8D%E2%99%82%EF%B8%8F.md)
* [Session 2🥧](../Session%20Notes/Session%202%F0%9F%A5%A7.md)
* [Session 3🦀](../Session%20Notes/Session%203%F0%9F%A6%80.md)
* [Session 4👠](../Session%20Notes/Session%204%F0%9F%91%A0.md)
* [Session 5💣](../Session%20Notes/Session%205%F0%9F%92%A3.md)
* [Session 6🎡](../Session%20Notes/Session%206%F0%9F%8E%A1.md)
* [Session 7🦷](../Session%20Notes/Session%207%F0%9F%A6%B7.md)
* [Session 8🖼️](../Session%20Notes/Session%208%F0%9F%96%BC%EF%B8%8F.md)
* [Session 9🐙](../Session%20Notes/Session%209%F0%9F%90%99.md)
* [Session Notes](/session-notes/session-notes)
* [Session Template](/templates/session-template)
