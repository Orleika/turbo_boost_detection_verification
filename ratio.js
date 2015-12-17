(function() {
  'use strict';

  var off = [1067.15, 19801.85, 1991.1, 12557.25, 29397.4, 14804.1, 7162.5, 16003.35, 5427.65, 19429.3];
  var on = [2331.55, 28678.1, 12896.65, 18410.5, 21798.5, 23514.7, 10719.1, 21802.7, 12252.85, 46023.6];

  var len = off.length;
  var i, j;
  var r_off = [], r_on = [];
  for (i = 0; i < len; i++) {
    r_off[i] = [];
    r_on[i] = [];
    for (j = 0; j < len; j++) {
      r_off[i][j] = off[i] / off[j];
      r_on[i][j] = on[i] / on[j];
    }
  }

  var d_off = [], d_on = [];
  for (i = 0; i < len; i++) {
    d_off = [];
    d_on = [];
    for (j = 0; j < len; j++) {
      d_off.push(r_off[i][j]);
      d_on.push(r_on[i][j]);
    }
    console.log(d_on.join('\t'));
  }
}());
