var result = db.origin.find({"model": {$ne: ""}}, {
  "model": 1,
  "http_User-Agent": 1,
  "octane_RegExp": 1,
  "octane_Mandreel": 1,
  "octane_Crypto": 1,
  "octane_EarleyBoyer": 1,
  "octane_PdfJS": 1,
  "octane_MandreelLatency": 1,
  "octane_Box2D": 1,
  "octane_CodeLoad": 1,
  "octane_Gameboy": 1,
  "octane_Richards": 1,
  "octane_Typescript": 1,
  "octane_RayTrace": 1,
  "octane_NavierStokes": 1,
  "octane_DeltaBlue": 1,
  "octane_Splay": 1,
  "octane_SplayLatency": 1,
  "octane_zlib": 1,
  "octane_score": 1,
  "4thUpdate": 1,
  "5thUpdate": 1
});
DBQuery.shellBatchSize = result.count();
shellPrint(result);
