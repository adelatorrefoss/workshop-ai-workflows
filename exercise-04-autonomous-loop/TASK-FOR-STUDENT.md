# Student challenge — Fix a rule through a bounded autonomous loop

Repair the registration validator so that complete registrations for both `Introduction` and `Advanced` are accepted, while blank names, malformed emails, and unknown courses are rejected.

Give the agent authority to inspect failures, change the implementation, and validate again, but limit it to three total attempts. Do not coach it between attempts and do not permit changes that weaken the checks or narrow the required behavior.

The result must either be a green, generalized business-rule fix or a clearly diagnosed failure stopped at the attempt limit. Account for every correction made by the loop.
