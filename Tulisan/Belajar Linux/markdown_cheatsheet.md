<a name="section1"></a>
# Headings 1 #
## Headings 2 ##
### Headings 3 ###
#### Headings 4 ####
##### Headings 5 #####
###### Headings 6 ######

---

#####Basic Styles#####

- **Bold** 
- *Italic*
- ***bold + italic***
- Headings 1, 2, 3
- ~~strikethrough~~

---

#####Lists#####

1. Ordered List
	- Unordered sub Lists
	- Unordered sub Lists 2 
2. Ordered List 2
	a. Ordered sub lists
	2. Ordered sub lists 2

---

#####Links#####

- [I'm an inline-style link](https://www.google.com)
- [I'm an inline-style link with title](https://www.google.com "Google's Homepage")
- [I'm a reference-style link][reference text]
- [You can use numbers for reference-style link definitions][1]
- [link text itself]
- [Internal Link: go to first section](#section1)
- sample image: ![sample image](md_img\sample.png "Sample Image")

[reference text]: https://www.mozilla.org "Mozilla"
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com "Reddit"

---

#####Code Blocks#####

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

`Highlights`

---

#####Tables#####
| Tables        | Are           |     Cool      |
| ------------- |:-------------:| -------------:|
| col is        | centered      | right-aligned |
| col doesn't | need to | be aligned |
| *in table* | **markdown**      |    `are neat` |

***Rule***: There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up. You can also use inline Markdown.

:--: means centered, --: means right-aligned

---

#####Blockquotes#####
> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure

---
#####Inline/Raw HTML#####

<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work. Use HTML <em>tags</em> instead.</dd>
</dl>

<del>strikethrough</del>

---

#####Separator#####
---
or 
***
or
___
