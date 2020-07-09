# APU_logs

## usage
<b>python3 logparser.py <FileName></b>
  
  lists present [ERROR TYPE - SCSI OPERATION CODE] tuples
  
  example:
  ```
  [root@mtr-apu-logs:/home/matous.trnka/APU_logs] python3 logparser.py ../PC-1768_na1_cmp0131.log
  Present error types in this file, format: (<ErrorType>,<SCSIOperationCode>):
  ('0x01', '0x1a')
  ('0x01', '0x5a')
  ('0x01', '0x2a')
  ('0x01', '0x00')
  ('0x01', '0x28')
  ```

python3 logparser.py <FileName> <ErrorType> [<SCSIOperationCode>]
  
  lists drive positions and number of errors of those drives that contains specified error type (and scsi code)
  
  example:
  ```
  [root@mtr-apu-logs:/home/matous.trnka/APU_logs] python3 logparser.py ../PC-1768_na1_cmp0131.log 0x01 0x1a
  1I:3:4                        75 (0x0000004b)
  1I:3:3                        75 (0x0000004b)
  1I:3:2                        75 (0x0000004b)
  1I:3:1                        75 (0x0000004b)
  2I:3:5                        75 (0x0000004b)
  2I:3:6                        75 (0x0000004b)
  2I:3:7                        75 (0x0000004b)
  2I:3:8                        75 (0x0000004b)
  3I:2:4                        75 (0x0000004b)
  3I:2:3                        75 (0x0000004b)
  3I:2:2                        75 (0x0000004b)
  3I:2:1                        74 (0x0000004a)
  4I:2:5                        72 (0x00000048)
  4I:2:6                        74 (0x0000004a)
  4I:2:7                        73 (0x00000049)
  4I:2:8                        74 (0x0000004a)
  ```
