---
title: CON for iEEG @ DHMC group

---

# CON for iEEG @ DHMC group

## Prior pointers

"intracranial electrophysiology meeting"

>    I hope all is well. Our Dartmouth/DH Human Intracranial
   Electrophysiology Consortium would like to invite you to give a talk at
   one of our monthly meetings. Our next meeting will take place via Zoom
   from 1:00 to 2:00 PM on September 11, 2026.

> Thank you for proposing the various topics and we would love to have Cody talk about NWB. Nonetheless, topics on data standards, data management, and reproducibility would be very helpful to our group.

> @Krzysztof A. Bujarski, do we have any prior recordings of our past meetings? In terms of the audience, our human intracranial group primarily collects data from epilepsy patients (performing computer-based tasks) undergoing
> intracranial EEG investigation. Some of the PIs involved in this group include Kris Bujarski, Caroline Robertson, Wilder Doucette, Arjen Stolk, Tor Wager, and me. We all use various tools for analysis (python, R, and matlab
> packages) and preprocessing. I anticipate some questions on the best practices (and not too onerous) we can undertake as a group to standardize the outputs of individual analysis steps (preprocessing versus
> experiment-specific analyses) such that someone else who is not involved in the experiment/analysis can examine, understand, and replicate (or not) the results with little effort.

>    Thank you very much for agreeing to present at our group’s meeting.
   October 9^th at 1 PM would be perfect if you could make it.   As
   Richard may have told you, we collect human intracranial EEG data for
   research purposes.  Right now it is macroelectrodes but soon it will
   also be microelectrodes with larger storage and data handling needs.
   We would be most interested in hearing about what you do and how you go
   about handling data in general.  We have not been saving our video
   meetings but generally 10-15 people meet over Zoom and discuss a
   research project or we have a conversation about a specific topic.
   Happy to talk to you if you would like more context.



Target ~40 minutes for talk, leave lots of time for questions/discussion


## Points

- May be start the talk with mission statement of discovering from their questions/feedback on how they do research and where "our" products could help
    - clarifications Qs are good, BIG - till Q&A
    - Drive or thread with "Reasons" as "Why?" any particular thing should be adopted/used
    - "many sizes fit all" -- not 1 solution, but a "toolbelt" and many ways to assemble without "buying in 100%"
        - relate to maturity model plot, may be use it as the umbrella to thread under?

- Focus on high-level concepts:
  - BI **Archives**
    - Mainly OpenNeuro/NEMAR, talk about your repronim work? mention future of EMBER & BBQS
    - reasons AKA why good: "free backup", "open by design" [ref]
  - **Standards** as enabler for tooling:
      - Oliver's poster to bring them all together
          - from single file format into datasets
      - BIDS data structure and HED annotations within (and on NEMAR)
          - point to AI tools to come up with annotations
          - seek their input on how THEY do preprocessing
      - NWB 
          - neurosift demos (will have to mostly be GIFs on DANDI data)
              - accent: stream based, no need to download
              - open-source
          - Cody's plugins on LFP (event related) and spectrograms
            - Example 1 (LFP only): https://openneuro.org/datasets/ds008610/versions/1.0.0/file-display/sub-01:ses-ieeg01:ieeg:sub-01_ses-ieeg01_task-FUS_acq-VPL_run-005_ieeg.nwb
            - Not finding any others
  - **RDM** Data Management (DataLad get, run/rerun, containers)
      - **must** have reason(s) stated
  - STAMPED principles (which we then keep coming back)
      - Brief overview + pointer to BBQS talk
      - Relate to FAIR they have likely heard about (Cody's slide/part of poster)
      - Self-containment + Modularity: (Meta) BIDS-Study
          - point to https://github.com/brain-bbqs/study-template
          - demo OpenNeuroStudies and dandi-compute
      - STAMPED examples
  - Compute
      - dandi-compute
      - mechababs (enabler for BIDS datasets) and compute on Unity
  - Visions for the future: 
      - mass preprocessed data to be reused with confidence: both of those for "mass compute" to fascilitate future "meta-studies" or "multi-verse"
      - knowledge bases: from local (ORINOCOs) to EBRAIN KB, brainkb etc  and relation to STAMPED
      - 

- Map out the mind-tree of resources across projects
    - ReproNim: reproducible practices 
        - webinar series talks
        - reprotube copy with them
        - point to ReproNim fellows program
    - DANDI:
        - NeuroData AI accepting applications
    - EMBER [emphasize future, nothing available as of today]:
        - Synchronization (they are the experts to share expertiese)
        - Pozu: turnkey platform for pose estimation and behavioral annotations with integration into archives

- Map/remind any particular solution in terms of STAMPED and FAIR

### Messages

- "MVC" points to modularity with models for modules/components
- Open Source might allow
    - for local use whenever BRAIN archives use centrally
    - to collaborate with colleagues who do not have your proprietary solution
    - have issue reported & fixed
- "Cool stuff (visualization, turnkey apps) is possible only because of boring stuff (standards)"
- Bring up DICOM (Open Standard) standard as unifying factor for imaging and some physio
    - problem: when proprietary fields are used.
    - again not "all size fits all" but iterative improvements
- Bring up NWB as the unification of the wild-west in neurophysiology
    - neuroconv image for conversions...
    - They could become part of the larger DICOM ecosystem
        - point to WG-32 requests

