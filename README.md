# BTB-world-manager

The purpose of this is to run a world simulator that updates territories and the nations that control them.
This handles territory invasion and battle states as well as population increases, decreases or migrations.
This is all handled within the world object provided by the world maker, all actions are done within timed 
world turns, player can send interrupts for particular territories for which they are present, this 
essential pauses all actions until the player leaves. Player actions can change the outcome of battles and 
alter population and resources.

When territory maps enter certain states they will send requests to create or update game maps, these are
the actual maps used to make 3d game maps for the player to explore.

## ToDos
1. Given a world json load and start update cycle, this creates a new json every turn, provide ability to request new world if one does not exist
2. mark territories as locked when player is present, free the lock when player leaves. 
3. Territories in disputed state will have nation strengths for nations present. Game maps may update this strength once player leaves. Thus if all ally or enemy power is destroyed then the territory will be set a controlled by remaining power. If there is no player then randomized power deductions are applied to both powers till one reaches 0.
4. Population growth and migration can be applied each turn as well. 
5. Depending on population and territory type there is a random chance of adding development to the territory
6. If a territory is changed then it is added to a change list that can be later sent off for creating new game maps if needed.
## Future Work
- Individual territory resources and climate/weather influence
- Handling of infrastructure upgrades and possible proximity effect.
