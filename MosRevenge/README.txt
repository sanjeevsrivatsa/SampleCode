Solution to this challenge:
An angry bird named Mo is flying a long journey to exact his revenge on the pigs. To save energy for the fight, the bird will take advantage of jet streams that will lower his flying energy consumption. Before the flight, BirdHQ gave the bird an input file in the following format:

    First line contains only 1 integer, which is the constant energy it takes to fly 1 mile WITHOUT jet streams.
        Every subsequent line contains 3 space-separated integers: the start mile marker of the jet stream, the end mile marker of the jet stream, and lastly an integer denoting the overall energy needed to fly that jet stream’s distance.

        For instance, the line “3 7 12″ means it takes 12 energy units to fly the 4 miles between miles 3 and 7.

        Note that jet streams can overlap, but the bird cannot be on more than one jet stream at a time, and it cannot fly partial jet streams.

        For simplicity, consider the end mile marker of the farthest jet stream as the end of the journey.

        Write a python program that takes in an input file jetstreams.txt to plan out the optimal sequence of jet streams Mo should fly on to minimize his energy consumption throughout the entire journey. All integers in the input file are non-negative. As output, print out the mininum total energy and a list of tuples denoting the jet streams’ endpoints.

        For example, given this sample jetstreams.txt, the minimum total energy needed to fly all 24 miles is 352 energy units, and the optimal sequence of jet streams is [(0,5), (6,11), (14,17), (19,24)].
