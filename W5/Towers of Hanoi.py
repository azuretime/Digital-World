def move_disks(n, fromTower, toTower, auxTower, sol):
    if n==1:
        sol.append('Move disk %d from %s to %s'%(n, fromTower, toTower))
    else:
        move_disks(n-1, fromTower, auxTower, toTower, sol)
        sol.append('Move disk %d from %s to %s'%(n, fromTower, toTower))
        move_disks(n-1, auxTower, toTower, fromTower, sol)

def move_disks(n, fromTower, toTower, auxTower, sol):
    
    if n >= 1:
        move_disks(n-1,fromTower,auxTower,toTower,sol)
        sol.append("Move disk %d from %s to %s" %(n,fromTower,toTower))
        move_disks(n-1,auxTower,toTower,fromTower,sol)

