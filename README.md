# The Skyrmion Dome Repository

Just a place to hold some code for a paper on skyrmion domes in thick films + checklists and some results

## Reading

Review spin transfer torque, then look back over spin statistics and reread Zhang and Li

## Checklist/Plan

1.  Double dome height and run current for longer
    a.  Try relaxing the system after a split has ocurred
    
2.  Surprisingly the height of the split seems independent of the height of the dome! Check this, try making the film 300nm and the dome 200nm
    a.  It seems to slice off the top part of the dome but always leaves the bottom 30nm

3.  Try blowing off this top part to leave the bottom 30nm, then after the top part is gone relax what's left and see what happens:
    a.  If there is something left try pushing some more current through and see what you get - might need a lot of curret
    b.  If something unexpected happens when relaxing just use what's left of the previous run and push some more current
    
3.  Figure out in-slurm script variables to reduce possibility of inconsistent core usage on the cluster

## Next Steps

**We might want to try "relaxing" the dome with a current: use the cylinder as initial magnetization and see what happens if we simply run zero current and a lot of dissipation alpha**

1.  Try running small currents (~1,2,3) with a large damping parameter to impose numerical stability

2.  Try making a dome on the *side* of the sample and running a current to see if the height of the dome can be altered

3.  Find new critical current with large damping parameter
    a.  Might need to fun concurrently with cluster to speed up process...wtf is the cluster so slow - lower core usage to save billing units

**Ideally we should get that the "birthing" that the relaxed dome will do can be engineered to happen successively at a known current. *And* we should have a good idea of what the stability landscape is as we increase the current**

Reread this readme and reorganize...I can't keep track of all the little experiments going on and I need to find a better way to do so + what are the results?


Here's a composite of a dome at various depths
![compositeSkyrmionDepth](https://user-images.githubusercontent.com/74024926/151843302-36616cc4-1cac-46bd-99ac-640567006241.png)

Here is a 3D rendition of the dome profile made with Blender
![skyrmionDome4](https://user-images.githubusercontent.com/74024926/151843738-cbc5f439-74a9-4815-a828-59b986dfe383.png)

Actually an idea for a project is an addon for Blender that facilitates graphinc vector fields
