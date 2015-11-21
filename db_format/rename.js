var result = db.lancers.update({}, {
    $rename: {
      "octane_Typescript": "Typescript",
      "octane_Richards": "Richards",
      "octane_DeltaBlue": "DeltaBlue",
      "octane_Crypto": "Crypto",
      "octane_RayTrace": "RayTrace",
      "octane_EarleyBoyer": "EarleyBoyer",
      "octane_RegExp": "RegExp",
      "octane_Splay": "Splay",
      "octane_SplayLatency": "SplayLatency",
      "octane_NavierStokes": "NavierStokes",
      "octane_PdfJS": "PdfJS",
      "octane_Mandreel": "Mandreel",
      "octane_MandreelLatency": "MandreelLatency",
      "octane_Gameboy": "Gameboy",
      "octane_CodeLoad": "CodeLoad",
      "octane_Box2D": "Box2D",
      "octane_zlib": "zlib",
      "octane_score": "totalScore"
    },
  }
  "upsert": false,
  "multi": true
);
DBQuery.shellBatchSize = result.count();
shellPrint(result);
