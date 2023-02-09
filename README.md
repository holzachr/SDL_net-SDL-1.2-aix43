# SDL_net-SDL-1.2-aix43

An attempt of porting SDL-1.2 extensions to AIX 4.3.3.
Feel free to use it for porting your favorite application to RS/6000!

Releases are compiled using xlC 6.0 for small footprint and maximum optimization.

# Installation

Check out https://github.com/holzachr/SDL-1.2.16-aix43/releases

# Limitations

None known.

# Building

If you want to replicate:

```
. xlc-env-settings-aix43-ppc.sh
./configure --with-sdl-prefix=/opt/SDL --prefix=/opt/SDL
make
make install
```

# License

Check the contained COPYING file for the authors' rights.
