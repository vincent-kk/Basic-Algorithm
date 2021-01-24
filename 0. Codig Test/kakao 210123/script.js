const run = (e) => {
  const num = 3;
  switch (num) {
    case 1:
      let input11 = 1;
      let input12 = [
        "1 fracta",
        "1 sina",
        "1 hana",
        "1 robel",
        "1 abc",
        "1 sina",
        "1 lynn",
      ];

      let output1 = solution1(input11, input12);
      console.log(output1);
      return;
    case 2:
      let input21 = 4;
      let input22 = [3, 2, 4, 1];
      let output2 = solution2(input21, input22);
      console.log(output2);
      return;
    case 3:
      let input3 = [5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2];
      let output3 = solution3(input3);
      console.log(output3);
      return;
    default:
      break;
  }
};

function solution1(n, record) {
  const servers = [[]];
  let answer = [];
  record.forEach((element) => {
    log = element.split(" ");
    num = log[0];
    nickname = log[1];
    if (!servers[num]) servers[num] = [];
    if (!servers[num].includes(nickname)) servers[num].push(nickname);
    if (servers[num].length > 5) servers[num] = servers[num].slice(1);
  });

  servers.forEach((server) => {
    server.forEach((user) => {
      answer.push(user);
    });
  });
  return answer;
}

function solution2(m, v) {
  const tetris = new Array();
  let level = 0;
  tetris[0] = m;
  v.forEach((block) => {
    for (let i = level; i >= 0; i--) {
      if (tetris[i] < block) {
        if (level < i + 1) {
          level++;
          tetris[i + 1] = m - block;
        } else {
          tetris[i + 1] = tetris[i + 1] - block;
        }
        return;
      }
    }
    tetris[level] = tetris[level] - block;
    // for (let l in tetris) {
    //   if (floor > l) continue;
    //   if (tetris[l] < block) {
    //     if (level == l) {
    //       level++;
    //       tetris.push(m - block);
    //       if (block === m) floor = level;
    //     }
    //   } else {
    //     tetris[l] = tetris[l] - block;
    //     break;
    //   }
    // }
  });

  return level + 1;
}

function solution3(next_student) {
  const size = next_student.length;
  const route = new Array(size);
  let temp = [];
  const calcRoute = (routeMap, target) => {
    if (temp.includes(target)) return 0;
    temp.push(target);
    if (routeMap[target] === 0) route[target] = 1;
    if (!route[target])
      route[target] = calcRoute(routeMap, routeMap[target] - 1) + 1;
    return route[target];
  };
  for (let i = 0; i < size; i++) {
    route[i] = calcRoute(next_student, i);
    temp = [];
  }

  let maxRoute = 0;
  let maxRouteStudent = 0;
  for (let i = 0; i < size; i++) {
    maxRouteStudent = maxRoute > route[i] ? maxRouteStudent : i;
  }
  return maxRouteStudent;
}
