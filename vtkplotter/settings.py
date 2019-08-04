"""
Global settings.

.. role:: raw-html-m2r(raw)
   :format: html

.. note:: **Please check out the** `git repository <https://github.com/marcomusy/vtkplotter>`_.

    A full list of examples can be found in directories:

    - `examples/basic <https://github.com/marcomusy/vtkplotter/blob/master/examples/basic>`_ ,
    - `examples/advanced <https://github.com/marcomusy/vtkplotter/blob/master/examples/advanced>`_ ,
    - `examples/volumetric <https://github.com/marcomusy/vtkplotter/blob/master/examples/volumetric>`_,
    - `examples/simulations <https://github.com/marcomusy/vtkplotter/blob/master/examples/simulations>`_.
    - `examples/other <https://github.com/marcomusy/vtkplotter/blob/master/examples/other>`_
    - `examples/other/dolfin <https://github.com/marcomusy/vtkplotter/blob/master/examples/other/dolfin>`_.

:raw-html-m2r:`<br />`

.. image:: https://user-images.githubusercontent.com/32848391/51558920-ec436e00-1e80-11e9-9d96-aa9b7c72d58b.png

:raw-html-m2r:`<br />`
:raw-html-m2r:`<br />`

"""
__all__ = ['datadir', 'embedWindow']

####################################################################################
# Axes titles
xtitle = 'x'
ytitle = 'y'
ztitle = 'z'

# Scale magnification of the screenshot (must be an integer)
screeshotScale = 1

screenshotTransparentBackground = False

# Recompute vertex and cell normals
computeNormals = None

# Default style is TrackBallCamera
interactorStyle = None

# Allow to interact with scene during interactor.Start() execution
allowInteraction = True

# Use tex, matplotlib latex compiler
usetex = False

# Qt embedding
usingQt = False

# OpenVR rendering
useOpenVR = False

# On some vtk versions/platforms points are redered as ugly squares
renderPointsAsSpheres = True

# Wrap lines in tubes
renderLinesAsTubes = False

# Remove hidden lines when in wireframe mode
hiddenLineRemoval = False

# For (Un)Structured and RectilinearGrid: show internal edges not only outline
visibleGridEdges = False

# Turn on/off the automatic repositioning of lights as the camera moves.
lightFollowsCamera = False

# Turn on/off nvidia FXAA anti-aliasing, if supported
useFXAA = False

# Turn on/off rendering of translucent material with depth peeling technique.
useDepthPeeling = False

# Path to Voro++ library, http://math.lbl.gov/voro++
voro_path = '/usr/local/bin'




####################################################################################
# notebook support with K3D
notebookBackend = None
notebook_plotter = None

####################################################################################
import os
_cdir = os.path.dirname(__file__)
if _cdir == "":
    _cdir = "."
textures_path = _cdir + "/textures/"
textures = []

datadir = _cdir + "/data/"
fonts_path = _cdir + "/fonts/"
fonts = []

def embedWindow(backend='k3d', verbose=True):
    global notebook_plotter, notebookBackend

    if not backend:
        notebookBackend = None
        notebook_plotter = None
        return

    notebookBackend = backend
    if backend=='k3d':

        try:
            get_ipython()
        except:
            notebookBackend = None
            return

        try:
            import k3d
            #if verbose:
            #    print('INFO: embedWindow(verbose=True), importing k3d module')
        except:
            notebookBackend = None
            if verbose:
                print('embedWindow(verbose=True): could not load k3d module, try:')
                print('> pip install k3d      # and/or')
                print('> conda install nodejs')

    elif backend=='panel':
        try:
            get_ipython()
            if verbose:
                print('INFO: embedWindow(verbose=True), first import of panel module, this takes time...')
            import panel
            panel.extension('vtk')
        except:
            if verbose:
                print('embedWindow(verbose=True): could not load panel try:')
                print('> pip install panel    # and/or')
                print('> conda install nodejs')
    else:
        print("Unknown backend", backend)
        raise RuntimeError()


#####################
def _init():
    global plotter_instance, plotter_instances, collectable_actors
    global textures, fonts
    global notebookBackend, notebook_plotter

    plotter_instance = None
    plotter_instances = []
    collectable_actors = []

    for f in os.listdir(textures_path):
        textures.append(f.split(".")[0])
    textures.remove("earth")
    textures = list(sorted(textures))

    for f in os.listdir(fonts_path):
        fonts.append(f.split(".")[0])
    fonts.remove("licenses")
    fonts = list(sorted(fonts))

    import warnings
    warnings.simplefilter(action="ignore", category=FutureWarning)

    embedWindow()



