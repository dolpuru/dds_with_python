Queue queue = create_queue();
Position cur;
cur.x = 0;
cur.y = 0;
enqueue(queue, cur);
maze[0][0] = -1; //추가 배열을 쓰지 않기 위해서 방문 표시를음수로 저장
bool found = false;
while (!is_empty(queue))
{
    Position cur = dequeue(queue);
    for (int dir = 0; dir < 4; dir++)
    {
        if (movable(cur, dir))
        {
            Position p = move_to(cur, dir);
            maze[p.x][p.y] = maze[cur.x][cur.y] - 1;
            if (p.x == n - 1 && p.y == n - 1)
            {
                printf("Found the path.\n");
                found = true;
                break;
            }
            enqueue(queue, p);
        }
    }
}