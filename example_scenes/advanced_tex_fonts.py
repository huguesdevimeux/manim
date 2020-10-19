from manim import *

# French Cursive LaTeX font example from http://jf.burnol.free.fr/showcase.html

# Example 1 Manually creating a Template

TemplateForFrenchCursive = TexTemplate(
    preamble=r"""
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[T1]{fontenc}
\usepackage[default]{frcursive}
\usepackage[eulergreek,noplusnominus,noequal,nohbar,%
nolessnomore,noasterisk]{mathastext}
"""
)


def FrenchCursive(*tex_strings, **kwargs):
    return Tex(*tex_strings, tex_template=TemplateForFrenchCursive, **kwargs)


class TexFontTemplateManual(Scene):
    """An example scene that uses a manually defined TexTemplate() object to create
    LaTeX output in French Cursive font"""

    def construct(self):
        self.add(Tex("Tex Font Example").to_edge(UL))
        self.play(ShowCreation(FrenchCursive("$f: A \\longrightarrow B$").shift(UP)))
        self.play(
            ShowCreation(FrenchCursive("Behold! We can write math in French Cursive"))
        )
        self.wait(1)
        self.play(
            ShowCreation(
                Tex(
                    "See more font templates at \\\\ http://jf.burnol.free.fr/showcase.html"
                ).shift(2 * DOWN)
            )
        )
        self.wait(2)


# Example 2, using a Template from the collection


class TexFontTemplateLibrary(Scene):
    """An example scene that uses TexTemplate objects from the TexFontTemplates collection
    to create sample LaTeX output in every font that will compile on the local system.

    Please Note:
    Many of the in the TexFontTemplates collection require that specific fonts
    are installed on your local machine.
    For example, choosing the template TexFontTemplates.comic_sans will
    not compile if the Comic Sans Micrososft font is not installed.

    This scene will only render those Templates that do not cause a TeX
    compilation error on your system. Furthermore, some of the ones that do render,
    may still render incorrectly. This is beyond the scope of manim.
    Feel free to experiment.
    """

    def construct(self):
        def write_one_line(template):
            x = Tex(template.description, tex_template=template).shift(UP)
            self.play(ShowCreation(x))
            self.wait(1)
            self.play(FadeOut(x))

        examples = [
            TexFontTemplates.american_typewriter,  # "American Typewriter"
            # "Antykwa Półtawskiego (TX Fonts for Greek and math symbols)"
            TexFontTemplates.antykwa,
            TexFontTemplates.apple_chancery,  # "Apple Chancery"
            # "Auriocus Kalligraphicus (Symbol Greek)"
            TexFontTemplates.auriocus_kalligraphicus,
            TexFontTemplates.baskervald_adf_fourier,  # "Baskervald ADF with Fourier"
            TexFontTemplates.baskerville_it,  # "Baskerville (Italic)"
            TexFontTemplates.biolinum,  # "Biolinum"
            # "BrushScriptX-Italic (PX math and Greek)"
            TexFontTemplates.brushscriptx,
            TexFontTemplates.chalkboard_se,  # "Chalkboard SE"
            TexFontTemplates.chalkduster,  # "Chalkduster"
            TexFontTemplates.comfortaa,  # "Comfortaa"
            TexFontTemplates.comic_sans,  # "Comic Sans MS"
            TexFontTemplates.droid_sans,  # "Droid Sans"
            TexFontTemplates.droid_sans_it,  # "Droid Sans (Italic)"
            TexFontTemplates.droid_serif,  # "Droid Serif"
            # "Droid Serif (PX math symbols) (Italic)"
            TexFontTemplates.droid_serif_px_it,
            TexFontTemplates.ecf_augie,  # "ECF Augie (Euler Greek)"
            TexFontTemplates.ecf_jd,  # "ECF JD (with TX fonts)"
            TexFontTemplates.ecf_skeetch,  # "ECF Skeetch (CM Greek)"
            # "ECF Tall Paul (with Symbol font)"
            TexFontTemplates.ecf_tall_paul,
            TexFontTemplates.ecf_webster,  # "ECF Webster (with TX fonts)"
            TexFontTemplates.electrum_adf,  # "Electrum ADF (CM Greek)"
            TexFontTemplates.epigrafica,  # Epigrafica
            # "Fourier Utopia (Fourier upright Greek)"
            TexFontTemplates.fourier_utopia,
            TexFontTemplates.french_cursive,  # "French Cursive (Euler Greek)"
            TexFontTemplates.gfs_bodoni,  # "GFS Bodoni"
            TexFontTemplates.gfs_didot,  # "GFS Didot (Italic)"
            TexFontTemplates.gfs_neoHellenic,  # "GFS NeoHellenic"
            # "GNU FreeSerif (and TX fonts symbols)"
            TexFontTemplates.gnu_freesans_tx,
            TexFontTemplates.gnu_freeserif_freesans,  # "GNU FreeSerif and FreeSans"
            # "Helvetica with Fourier (Italic)"
            TexFontTemplates.helvetica_fourier_it,
            # "Latin Modern Typewriter Proportional (CM Greek) (Italic)"
            TexFontTemplates.latin_modern_tw_it,
            TexFontTemplates.latin_modern_tw,  # "Latin Modern Typewriter Proportional"
            TexFontTemplates.libertine,  # "Libertine"
            TexFontTemplates.libris_adf_fourier,  # "Libris ADF with Fourier"
            # "Minion Pro and Myriad Pro (and TX fonts symbols)"
            TexFontTemplates.minion_pro_myriad_pro,
            # "Minion Pro (and TX fonts symbols)"
            TexFontTemplates.minion_pro_tx,
            # "New Century Schoolbook (Symbol Greek)"
            TexFontTemplates.new_century_schoolbook,
            # "New Century Schoolbook (Symbol Greek, PX math symbols)"
            TexFontTemplates.new_century_schoolbook_px,
            TexFontTemplates.noteworthy_light,  # "Noteworthy Light"
            TexFontTemplates.palatino,  # "Palatino (Symbol Greek)"
            TexFontTemplates.papyrus,  # "Papyrus"
            # "Romande ADF with Fourier (Italic)"
            TexFontTemplates.romande_adf_fourier_it,
            TexFontTemplates.slitex,  # "SliTeX (Euler Greek)"
            TexFontTemplates.times_fourier_it,  # "Times with Fourier (Italic)"
            # "URW Avant Garde (Symbol Greek)"
            TexFontTemplates.urw_avant_garde,
            # "URW Zapf Chancery (CM Greek)"
            TexFontTemplates.urw_zapf_chancery,
            # "Venturis ADF with Fourier (Italic)"
            TexFontTemplates.venturis_adf_fourier_it,
            TexFontTemplates.verdana_it,  # "Verdana (Italic)"
            # "Vollkorn with Fourier (Italic)"
            TexFontTemplates.vollkorn_fourier_it,
            # "Vollkorn (TX fonts for Greek and math symbols)"
            TexFontTemplates.vollkorn,
            TexFontTemplates.zapf_chancery,  # "Zapf Chancery"
        ]

        self.add(Tex("Tex Font Template Example").to_edge(UL))

        for font in examples:
            try:
                write_one_line(font)
            except:
                print("FAILURE on ", font.description, " - skipping.")

        self.play(
            ShowCreation(
                Tex(
                    "See more font templates at \\\\ http://jf.burnol.free.fr/showcase.html"
                ).shift(2 * DOWN)
            )
        )
        self.wait(2)
