# The Skyrmiond Dome Repository

Just a place to hold some code for a paper on skyrmion domes in thick films

## **Checklist/Plan**

1)  Double dome height and run current for longer
    a)  Try relaxing the system after a split has ocurred
    
2)  Surprisingly the height of the split seems independent of the height of the dome! Check this, try making the film 300nm and the dome 200nm
    a)  It seems to slice off the top part of the dome but always leaves the bottom 30nm

3)  Try blowing off this top part to leave the bottom 30nm, then after the top part is gone relax what's left and see what happens:
    a)  If there is something left try pushing some more current through and see what you get - might need a lot of curret
    b)  If something unexpected happens when relaxing just use what's left of the previous run and push some more current
    
3)  Figure out in-slurm script variables to reduce possibility of inconsistent core usage on the cluster

4)  Also read up on Markdown to make this thing prettier

## To Show on Friday 2/11
[x] Dragged dome: maybe 120nm dome dragged by low current density **Already done in u_35 folder

[x] Split dome 1: a dome at a higher current (~100) with multiple chunks

[x] Split dome 2: another dome of a different relaxed height to show that all domes spit at 30nm


Here's a composite of a dome at various depths
![compositeSkyrmionDepth](https://user-images.githubusercontent.com/74024926/151843302-36616cc4-1cac-46bd-99ac-640567006241.png)

Here is a 3D rendition of the dome profile made with Blender
![skyrmionDome4](https://user-images.githubusercontent.com/74024926/151843738-cbc5f439-74a9-4815-a828-59b986dfe383.png)

Actually an idea for a project is an addon for Blender that facilitates graphinc vector fields
