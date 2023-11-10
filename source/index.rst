====================
The Toeplitz Project
====================

Facilitating the genetic method in the study of mathematics
===========================================================

.. figure:: https://upload.wikimedia.org/wikipedia/commons/b/b4/Toeplitz.jpg
   :target: https://en.wikipedia.org/wiki/Otto_Toeplitz#/media/File:Toeplitz.jpg
   :align: right


.. epigraph::

   I would call this the *genetic method*. I...said to myself: all these
   components of the infinitesimal calculus...are taught today as part
   of a canonical syllabus, and nowhere is the question asked: Why so? How did
   one arrive at just these results? Each of these developments must have arisen
   from some exciting investigation, some impassioned search, at the time it was
   first invented. If we would only return to these roots of the concepts we
   teach, then would the dust of time and the wear of long use fall away, and
   they would be reborn to us as creatures full of life.

   -- `Otto Toeplitz`_, 1927_


Digitizing historical steps
===========================

While any academic subject can benefit from digitization of the early
documents in which the subject was formed, mathematics is special in that its
core artifact -- the mathematical proof -- is a form of logical argumentation
that can be broken down further, into *steps*.

The purpose of the Toeplitz Project is to facilitate historically
based teaching and learning in mathematics, by
providing a specialized digital resource, in which the proof steps
from the subject's historical documents are individually represented.


Method
======

Proofs from historical mathematical books and papers are translated by
expert, human translators into a system called Proofscape_. This is a simple
argument mapping system, tailored to the needs of mathematics.

In this translation, proofs are broken down into steps, while the form of the
argument, and the locations of cited sources, lemmas, and theorems, are
preserved.

Each step is represented by a *node*, and its contents may be encoded in
multiple ways, such as:

* In the original, natural language of publication (often French, German,
  Russian, or Latin).

* As an English translation, with use of modern notation.

* As objects and relations in the syntax of a computer algebra system.

* With links to source PDF documents.

Since Proofscape nodes are open-ended, more encodings than these may be
added.


Benefits
========

Representing proofs from the existing literature in the form
described above opens up myriad, powerful ways of using computers to enrich
the study of mathematics. For example:

* **Browsable archives:** Students can have the history of mathematics right
  at their fingertips, with the ability to call up any proof from any paper,
  and to read it in a language they understand.

* **A history of proof ideas:** By drawing connections between different papers
  in which proof ideas were introduced and replicated, students and scholars
  can begin to piece together a detailed history of the origin and evolution
  of such ideas.

* **Example generation:** A computer algebra system like SymPy_ can be used to
  generate numerical examples of the types of mathematical objects in
  play at any given step of a proof, thereby helping to illustrate the ideas.

* **Verification and interpolation:** A theorem prover like Lean_ can be used to check
  that the steps from the historical literature are valid -- and find those that
  were not -- and even to provide missing steps, omitted in original texts.

* **Annotations:** Teachers can use the PISE_ software to author *annotations*.
  These are discussions of proofs that are displayed side by side with a graphical
  display representing the steps of the proof. Clicking links in the discussion
  causes the proof graphics to navigate, advance, and light up, showing the part
  that's being discussed.

* **Expansions:** The PISE software can be used to display and hide *expansions*, which
  are collections of additional steps that can be spliced into proofs to fill in
  difficult inferential leaps.

* **Visualization:** The steps of each proof can be diagrammed in a way that reflects
  the deductive structure of the argument. This can yield immediate insight into the
  way the parts of the proof fit together, where the premises are used, and what are
  the key constructions. It can also aid in remembering proofs, by associating each
  step with a place in a visual, mental model.


What it's not
=============

A few remarks are in order, to head off possible misconceptions.

* **Not scanning documents:** Electronically scanning old documents to make PDFs is one very important step
  in preserving our mathematical heritage, but that is not a part of this project.

* **No emphasis on particular applications:** The purpose is to provide a library, which is a raw material that can be used
  in many ways, such as those discussed in the Benefits_ section above.

  In particular, while the Proofscape language was originally
  designed for visualizing proofs in diagrammatic form, and that is one
  capability the library will support, this is not central. In fact PISE_, the
  Proofscape browsing software, can also show the steps of proofs in simple
  linear order, and it is up to individual users to decide how they want to
  browse proofs.


Challenge goal: 100 year anniversary
======================================

Toeplitz published his paper on the genetic method in 1927.
It seems a worthwhile and attainable goal, to try to build this library into a
valuable resource for math students by 2027.


.. toctree::
   :maxdepth: 2
   :hidden:

   repos/index
   contrib/index



.. _Otto Toeplitz: https://en.wikipedia.org/wiki/Otto_Toeplitz
.. _1927: https://www.digizeitschriften.de/download/pdf/37721857X_0036/log7.pdf
.. _Proofscape: https://docs.proofscape.org/
.. _SymPy: https://sympy.org
.. _Lean: https://leanprover-community.github.io/
.. _PISE: https://docs.proofscape.org/pise/index.html
