### Touch the grass

*Toy idea for LangChain memory hackathon.*

#### Motivation (ambitious)

Endow powerful LLM agents with spatial memory using location history and access to notes, social circle, historical information to recreate memories for therapeutic, artistic or entertainment purpose.

<details><summary>pushing it...</summary>
You can plug in spatial memories of other people to activate "View As" type of experiences.
</details>

#### Motivation (smol)

Endow powerful LLM agents (here, `Claude Opus`) with spatial memory using location history and LLM-generated description from photos.

#### Use case: Mood companion

Given your current mood and location, `Claude` makes thoughtful suggestions to help change your mood based on your location history and corresponding mood using photos archive.

You feel stressed. You happen to be 10 min walk from your favorite sunset spot. `Claude` could suggest you take a walk and literally touch the grass and enjoy the sunset.

<details><summary></summary>
Clearly, these search suggestions can be much more interesting and elaborate based on customization.
</details>

##### Generate location & mood history
- Extract (precise) location and time information from apps (e.g., Google Maps Timeline) or personal photos

- Ask `Claude` to describe the photo given location and time
    - Infer semantic location given GPS coordinates
    - Ask (retrieve) weather given location and time
    - Describe 5 feelings conveyed in the photo (adjectives)

<details>
  <summary>Caveats</summary>
  
  - Location history from Google Maps is hit or miss depending on your settings.
  - If you have your location history turned on, Google provides `semantic inferred location` so you can skip GPS location.
  - `Claude` API does not allow image URLs as input (yet)

</details>


##### Ask `Claude` to make suggestions
- Describe current mood
- Use function calling to find current location and weather
- Search location history to get reasonably close locations (e.g., <10-15 min walk, <30-45 min drive)
- Make suggestions based on time, weather, target mood and scenic descriptions
