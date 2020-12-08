## Fontbakery report

Fontbakery version: 0.7.33

<details>
<summary><b>[1] Family checks</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Is the command `ftxvalidator` (Apple Font Tool Suite) available?</summary>

* [com.google.fonts/check/ftxvalidator_is_available](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ftxvalidator_is_available)
<pre>--- Rationale ---

There&#x27;s no reasonable (and legal) way to run the command `ftxvalidator` of the
Apple Font Tool Suite on a non-macOS machine. I.e. on GNU+Linux or Windows etc.

If Font Bakery is not running on an OSX machine, the machine running Font
Bakery could access `ftxvalidator` on OSX, e.g. via ssh or a remote procedure
call (rpc).

There&#x27;s an ssh example implementation at:
https://github.com/googlefonts/fontbakery/blob/master/prebuilt/workarounds
/ftxvalidator/ssh-implementation/ftxvalidator


</pre>

* ⚠ **WARN** Could not find ftxvalidator.

</details>
<br>
</details>
<details>
<summary><b>[10] KiwiMaru-Light.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Kiwi Maru Light" but got "キウイ 丸". [code: mismatch]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---

Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is
stored in the achVendID field of the OS/2 table.

Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:

https://docs.microsoft.com/en-us/typography/vendors/

This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.

Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.


</pre>

* ⚠ **WARN** OS/2 VendorID value 'KWKK' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: X	Contours detected: 2	Expected: 1
Glyph name: beta	Contours detected: 1	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: uni210A	Contours detected: 3	Expected: 2
Glyph name: infinity.full	Contours detected: 29	Expected: 3
Glyph name: uni255E	Contours detected: 1	Expected: 2
Glyph name: uni2561	Contours detected: 1	Expected: 2
Glyph name: X	Contours detected: 2	Expected: 1
Glyph name: beta	Contours detected: 1	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: uni210A	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + i
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font contains .notdef as first glyph?</summary>

* [com.google.fonts/check/mandatory_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs)
<pre>--- Rationale ---

The OpenType specification v1.8.2 recommends that the first glyph is the
.notdef glyph without a codepoint assigned and with a drawing.

https://docs.microsoft.com/en-us/typography/opentype/spec
/recom#glyph-0-the-notdef-glyph

Pre-v1.8, it was recommended that a font should also contain a .null, CR and
space glyph. This might have been relevant for applications on MacOS 9.


</pre>

* ⚠ **WARN** Font should contain the .notdef glyph as the first glyph, it should not have a Unicode value assigned and should contain a drawing.

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0300, U+0302, U+0303, U+0304, U+030A, U+0327, U+0332 and U+0336 [code: mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.


</pre>

* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+02CA and U+203E [code: non-mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---

This test heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed
up by manual inspection.


</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* X.rotat: L<<512.0,422.0>--<488.0,438.0>>/B<<488.0,438.0>-<489.0,437.0>-<482.0,431.0>> = 11.309932474020227
	* X: L<<458.0,392.0>--<442.0,368.0>>/B<<442.0,368.0>-<443.0,369.0>-<449.0,362.0>> = 11.309932474020227
	* delta: B<<578.0,501.5>-<606.0,497.0>-<637.0,468.0>>/B<<637.0,468.0>-<605.0,497.0>-<587.0,510.0>> = 0.9064042512144714
	* u2F80F: B<<194.0,465.0>-<194.0,497.0>-<222.0,512.0>>/B<<222.0,512.0>-<173.0,494.0>-<118.0,482.0>> = 8.007936698108741
	* u2F80F: B<<379.5,598.5>-<317.0,550.0>-<236.0,518.0>>/B<<236.0,518.0>-<239.0,519.0>-<242.0,519.0>> = 3.1221304621155834
	* uni0437: B<<616.5,264.0>-<594.0,251.0>-<582.0,250.0>>/B<<582.0,250.0>-<601.0,249.0>-<624.5,235.5>> = 7.776429194909452
	* uni24A4: B<<400.0,531.0>-<409.0,540.0>-<421.0,539.0>>/B<<421.0,539.0>-<417.0,539.0>-<414.0,539.5>> = 4.763641690726144
	* uni261D: L<<392.0,688.0>--<372.0,391.0>>/B<<372.0,391.0>-<377.0,408.0>-<383.5,424.0>> = 12.537054927054113
	* uni3047.vert: B<<561.0,400.0>-<596.0,433.0>-<611.0,458.0>>/B<<611.0,458.0>-<608.0,454.0>-<585.0,449.5>> = 5.906141113770435
	* uni3059.half.rotat: L<<416.0,605.0>--<430.0,605.0>>/B<<430.0,605.0>-<419.0,606.0>-<396.0,611.0>> = 5.1944289077348 and 113 more. [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---

This test detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.

This test is disabled for italic styles, which often contain nearly-upright
lines.


</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
	* B.rotat: L<<837.0,717.0>--<836.0,544.0>>
	* B: L<<163.0,717.0>--<336.0,716.0>>
	* Beta: L<<350.0,717.0>--<523.0,716.0>>
	* R.rotat: L<<836.0,703.0>--<835.0,520.0>>
	* R: L<<177.0,716.0>--<360.0,715.0>>
	* uni0412: L<<350.0,717.0>--<523.0,716.0>>
	* uni2520.half.rotat: L<<0.0,672.0>--<1000.0,673.0>>
	* uni2520.half.rotat: L<<1000.0,588.0>--<518.0,587.0>>
	* uni2520.half: L<<208.0,-120.0>--<207.0,880.0>>
	* uni2520.half: L<<292.0,880.0>--<293.0,398.0>> and 195 more. [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[11] KiwiMaru-Medium.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Kiwi Maru Medium" but got "キウイ 丸". [code: mismatch]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---

Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is
stored in the achVendID field of the OS/2 table.

Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:

https://docs.microsoft.com/en-us/typography/vendors/

This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.

Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.


</pre>

* ⚠ **WARN** OS/2 VendorID value 'KWKK' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: uni210A	Contours detected: 3	Expected: 2
Glyph name: infinity.full	Contours detected: 29	Expected: 3
Glyph name: uni255E	Contours detected: 1	Expected: 2
Glyph name: uni2561	Contours detected: 1	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: uni210A	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + i
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font contains .notdef as first glyph?</summary>

* [com.google.fonts/check/mandatory_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs)
<pre>--- Rationale ---

The OpenType specification v1.8.2 recommends that the first glyph is the
.notdef glyph without a codepoint assigned and with a drawing.

https://docs.microsoft.com/en-us/typography/opentype/spec
/recom#glyph-0-the-notdef-glyph

Pre-v1.8, it was recommended that a font should also contain a .null, CR and
space glyph. This might have been relevant for applications on MacOS 9.


</pre>

* ⚠ **WARN** Font should contain the .notdef glyph as the first glyph, it should not have a Unicode value assigned and should contain a drawing.

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0300, U+0302, U+0303, U+0304, U+030A, U+0327, U+0332 and U+0336 [code: mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.


</pre>

* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+02CA and U+203E [code: non-mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---

This test looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.

This test is not run for variable fonts, as they may legitimately have colinear
vectors.


</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* E.half.rotat: L<<702.0,521.0>--<760.0,516.0>> -> L<<760.0,516.0>--<762.0,516.0>>
	* E.half: L<<359.0,582.0>--<364.0,640.0>> -> L<<364.0,640.0>--<364.0,642.0>>
	* F.half.rotat: L<<702.0,521.0>--<760.0,516.0>> -> L<<760.0,516.0>--<762.0,516.0>>
	* F.half: L<<359.0,582.0>--<364.0,640.0>> -> L<<364.0,640.0>--<364.0,642.0>>
	* F.rotat: L<<186.0,778.0>--<184.0,756.0>> -> L<<184.0,756.0>--<184.0,754.0>>
	* F: L<<102.0,66.0>--<124.0,64.0>> -> L<<124.0,64.0>--<126.0,64.0>>
	* K.rotat: L<<185.0,778.0>--<183.0,750.0>> -> L<<183.0,750.0>--<183.0,748.0>>
	* K: L<<102.0,65.0>--<130.0,63.0>> -> L<<130.0,63.0>--<132.0,63.0>>
	* Kappa: L<<199.0,65.0>--<227.0,63.0>> -> L<<227.0,63.0>--<229.0,63.0>>
	* Psi: L<<861.0,636.0>--<828.0,639.0>> -> L<<828.0,639.0>--<826.0,639.0>> and 81 more. [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---

This test heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed
up by manual inspection.


</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* beta: B<<343.0,124.0>-<340.0,140.0>-<341.0,154.0>>/L<<341.0,154.0>--<260.0,-199.0>> = 8.837854626926458
	* uni0328.rotat: L<<117.0,741.0>--<117.0,630.0>>/B<<117.0,630.0>-<112.0,659.0>-<95.5,683.5>> = 9.782407031807285
	* uni0328: L<<139.0,-3.0>--<250.0,-3.0>>/B<<250.0,-3.0>-<221.0,-8.0>-<196.5,-24.5>> = 9.782407031807285
	* uni261C: B<<588.0,270.0>-<588.0,259.0>-<576.0,253.0>>/L<<576.0,253.0>--<589.0,259.0>> = 1.7899106082458724
	* uni261D: L<<621.0,291.0>--<627.0,304.0>>/B<<627.0,304.0>-<621.0,292.0>-<610.0,292.0>> = 1.7899106082458724
	* uni261E: L<<411.0,259.0>--<424.0,253.0>>/B<<424.0,253.0>-<412.0,259.0>-<412.0,270.0>> = 1.7899106082458724
	* uni261F: B<<610.0,468.0>-<621.0,468.0>-<627.0,456.0>>/L<<627.0,456.0>--<621.0,469.0>> = 1.7899106082458724
	* uni2FD4.jp78: B<<812.0,322.0>-<817.0,314.0>-<819.0,304.0>>/L<<819.0,304.0>--<819.0,323.0>> = 11.309932474020195
	* uni3082.half.rotat: L<<427.0,703.0>--<479.0,701.0>>/B<<479.0,701.0>-<477.0,701.0>-<475.0,703.0>> = 2.2025981617658017
	* uni3082.half: L<<177.0,307.0>--<179.0,359.0>>/B<<179.0,359.0>-<179.0,357.0>-<177.0,355.0>> = 2.2025981617658017 and 682 more. [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---

This test detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.

This test is disabled for italic styles, which often contain nearly-upright
lines.


</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
	* B.rotat: L<<849.0,705.0>--<848.0,532.0>>
	* B: L<<175.0,729.0>--<348.0,728.0>>
	* Beta: L<<350.0,729.0>--<523.0,728.0>>
	* R.rotat: L<<848.0,691.0>--<847.0,508.0>>
	* R: L<<189.0,728.0>--<372.0,727.0>>
	* uni0412: L<<350.0,729.0>--<523.0,728.0>>
	* uni0413: L<<393.0,727.0>--<697.0,728.0>>
	* uni2520.half.rotat: L<<-6.0,678.0>--<1006.0,679.0>>
	* uni2520.half.rotat: L<<1006.0,582.0>--<524.0,581.0>>
	* uni2520.half: L<<202.0,-126.0>--<201.0,886.0>> and 154 more. [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[11] KiwiMaru-Regular.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Kiwi Maru" but got "キウイ 丸". [code: mismatch]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---

Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is
stored in the achVendID field of the OS/2 table.

Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:

https://docs.microsoft.com/en-us/typography/vendors/

This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.

Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.


</pre>

* ⚠ **WARN** OS/2 VendorID value 'KWKK' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: beta	Contours detected: 1	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: uni210A	Contours detected: 3	Expected: 2
Glyph name: infinity.full	Contours detected: 29	Expected: 3
Glyph name: uni255E	Contours detected: 1	Expected: 2
Glyph name: uni2561	Contours detected: 1	Expected: 2
Glyph name: beta	Contours detected: 1	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: uni210A	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + i
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font contains .notdef as first glyph?</summary>

* [com.google.fonts/check/mandatory_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs)
<pre>--- Rationale ---

The OpenType specification v1.8.2 recommends that the first glyph is the
.notdef glyph without a codepoint assigned and with a drawing.

https://docs.microsoft.com/en-us/typography/opentype/spec
/recom#glyph-0-the-notdef-glyph

Pre-v1.8, it was recommended that a font should also contain a .null, CR and
space glyph. This might have been relevant for applications on MacOS 9.


</pre>

* ⚠ **WARN** Font should contain the .notdef glyph as the first glyph, it should not have a Unicode value assigned and should contain a drawing.

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0300, U+0302, U+0303, U+0304, U+030A, U+0327, U+0332 and U+0336 [code: mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.


</pre>

* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+02CA and U+203E [code: non-mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---

This test looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.

This test is not run for variable fonts, as they may legitimately have colinear
vectors.


</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* L.half.rotat: L<<775.0,663.0>--<777.0,685.0>> -> L<<777.0,685.0>--<777.0,687.0>>
	* L.half: L<<217.0,655.0>--<195.0,657.0>> -> L<<195.0,657.0>--<193.0,657.0>>
	* L.rotat: L<<188.0,780.0>--<185.0,750.0>> -> L<<185.0,750.0>--<185.0,748.0>>
	* L: L<<100.0,68.0>--<130.0,65.0>> -> L<<130.0,65.0>--<132.0,65.0>>
	* M.rotat: L<<180.0,791.0>--<177.0,758.0>> -> L<<177.0,758.0>--<177.0,756.0>>
	* M.rotat: L<<773.0,24.0>--<776.0,54.0>> -> L<<776.0,54.0>--<776.0,56.0>>
	* M: L<<856.0,653.0>--<826.0,656.0>> -> L<<826.0,656.0>--<824.0,656.0>>
	* M: L<<89.0,60.0>--<122.0,57.0>> -> L<<122.0,57.0>--<124.0,57.0>>
	* N.rotat: L<<180.0,785.0>--<177.0,751.0>> -> L<<177.0,751.0>--<177.0,749.0>>
	* N.rotat: L<<773.0,155.0>--<776.0,189.0>> -> L<<776.0,189.0>--<776.0,191.0>> and 48 more. [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---

This test heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed
up by manual inspection.


</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni51C4: B<<507.0,294.0>-<518.0,313.0>-<539.0,315.0>>/L<<539.0,315.0>--<379.0,315.0>> = 5.4403320310054815
	* uni530D: B<<648.0,517.0>-<641.0,507.0>-<626.0,505.0>>/L<<626.0,505.0>--<681.0,505.0>> = 7.594643368591447
	* uni550F: B<<449.0,247.0>-<449.0,274.0>-<469.0,292.0>>/B<<469.0,292.0>-<448.0,274.0>-<427.5,259.5>> = 1.3859178508119747
	* uni550F: B<<532.5,349.0>-<502.0,319.0>-<472.0,294.0>>/B<<472.0,294.0>-<489.0,307.0>-<509.0,307.0>> = 2.4002144608566436
	* uni5687: B<<674.5,113.0>-<686.0,185.0>-<690.0,282.0>>/B<<690.0,282.0>-<685.0,245.0>-<676.5,209.0>> = 5.334677063840902
	* uni56B4: B<<633.0,257.0>-<633.0,265.0>-<637.0,272.0>>/B<<637.0,272.0>-<614.0,239.0>-<590.0,216.0>> = 5.130447047659866
	* uni56B4: B<<669.0,324.0>-<655.0,300.0>-<641.0,278.0>>/B<<641.0,278.0>-<652.0,291.0>-<669.0,291.0>> = 7.765166018425354
	* uni56CE: B<<852.0,621.0>-<869.0,621.0>-<884.0,611.0>>/B<<884.0,611.0>-<856.0,637.0>-<831.5,666.0>> = 9.1888360773587
	* uni56CE: L<<893.0,603.0>--<892.0,604.0>>/B<<892.0,604.0>-<907.0,587.0>-<907.0,566.0>> = 3.5763343749974728
	* uni5831: B<<588.0,-36.0>-<585.0,-28.0>-<585.0,-22.0>>/B<<585.0,-22.0>-<584.0,-37.0>-<573.5,-47.0>> = 3.8140748342903783 and 210 more. [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---

This test detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.

This test is disabled for italic styles, which often contain nearly-upright
lines.


</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
	* B.rotat: L<<843.0,711.0>--<842.0,538.0>>
	* B: L<<169.0,723.0>--<342.0,722.0>>
	* Beta: L<<350.0,723.0>--<523.0,722.0>>
	* R.rotat: L<<842.0,697.0>--<841.0,514.0>>
	* R: L<<183.0,722.0>--<366.0,721.0>>
	* uni0412: L<<350.0,723.0>--<523.0,722.0>>
	* uni2520.half.rotat: L<<0.0,672.0>--<1000.0,673.0>>
	* uni2520.half.rotat: L<<1000.0,588.0>--<518.0,587.0>>
	* uni2520.half: L<<208.0,-120.0>--<207.0,880.0>>
	* uni2520.half: L<<292.0,880.0>--<293.0,398.0>> and 68 more. [code: found-semi-vertical]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 3 | 30 | 271 | 19 | 229 | 0 |
| 0% | 1% | 5% | 49% | 3% | 41% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
