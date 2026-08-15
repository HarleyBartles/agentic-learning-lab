# Technical drawing project

A project built around a real failure mode: asking a general-purpose cloud AI to create a technical drawing and getting an image-generation workflow instead of deterministic geometry.

Suggested structure as the exercise develops:

```text
technical-drawing/
    README.md
    specification/
    working/
    output/
```

Use this project to introduce the idea that intelligence and capability are separate. Later provision an appropriate drawing tool such as SVG generation, OpenSCAD, CAD tooling, or another deterministic geometry system, then add verification such as rendering or dimensional checks.

The important lesson is not which drawing tool wins. It is that the agent should be given a tool suited to the work and enough operating guidance to use it competently.
