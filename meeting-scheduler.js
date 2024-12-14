function meetingScheduler (meetings) {
    console.log(meetings);
    let start_time = meetings.map(meeting => meeting[0]);
    let end_time = meetings.map(meeting => meeting[1]);

    start_time.sort((a,b)=>a-b);
    end_time.sort((a,b)=>a-b);
    console.log(start_time, end_time);
    let strPtr = 0;
    let endPtr = 0;
    let count = 0;
    let rooms = 0;

    while(strPtr < start_time.length) {
        if(start_time[strPtr] < end_time[endPtr]) {
            count++;
            strPtr++;
        } else {
            count--;
            endPtr++;
        }
        rooms = Math.max(rooms, count);
    }
    return rooms;

}


console.log(meetingScheduler([[2,8], [3,9], [5,11], [3,4], [11,15], [8,20]]))