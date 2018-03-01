(TeX-add-style-hook
 "proposal"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "lmargin=1in" "rmargin=1in" "tmargin=1in" "bmargin=1in") ("hyphenat" "none")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "geometry"
    "enumitem"
    "hyphenat")
   (LaTeX-add-bibliographies
    "giraffe"))
 :latex)

