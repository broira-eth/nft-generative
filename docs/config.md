# Configuration
```
parts:
 - name: aaa
 - name: bbb
 - name: ccc

image:
  aaa:
    condition: false
    skip: false
    path: Output/Image/aaa

  bbb:
    condition: false
    skip: true

  ccc:
    condition: true
    skip: false
    related_parts: face
    path:
      face_a: Output/Image/ccc/face_a
      face_b: Output/Image/ccc/face_b

traits:
  path: Output/Metadata/traits.csv

size:
 height: 3000
 width: 3000
 ```
 ## parts
* Enumerate the part types, starting from the layer behind.
 ## image
* Specify the path to the image file of the part.

|attribute|description|
|-|-|
|condition|Whether the directory to be loaded changes depending on other parts.Used, for example, when there are different colours and the same part name.
|skip|Used when the image exists in the Trait but not in the image
|related_parts|Specifies which parts are dependent when Condition is True.
|path|Specify the directory where the part images are stored. The image file name must match the Trait.If the condition is True, it should be listed with the dependent Trait name like `face_a`.

 ## traits
* Specify the path to the traits file.
 ## size
 * Specify the size of the image to be combined.