# This file kills a process named killmenow
exec {'pkill killmenow':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  provider => 'shell',
}
