# BTB-world-manager

The purpose of this is to run a world simulator that updates territories and the nations that control them.
This handles territory invasion and battle states as well as population increases, decreases or migrations.
This is all handled within the world object provided by the world maker, all actions are done within timed 
world turns, player can send interrupts for particular territories for which they are present, this 
essential pauses all actions until the player leaves. Player actions can change the outcome of battles and 
alter population and resources.

When territory maps enter certain states they will send requests to create or update game maps, these are
the actual maps used to make 3d game maps for the player to explore.

## Future Work
- Individual territory resources and climate/weather influence
- Handling of infrastructure upgrades and possible proximity effect.
