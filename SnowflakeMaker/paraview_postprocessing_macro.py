# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
result_ = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1072, 782]

# get display properties
result_Display = GetDisplayProperties(result_, view=renderView1)

# set scalar coloring
ColorBy(result_Display, ('POINTS', 'phi'))

# rescale color and/or opacity maps used to include current data range
result_Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
result_Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'phi'
phiLUT = GetColorTransferFunction('phi')
phiLUT.RGBPoints = [-1.0, 0.301961, 0.047059, 0.090196, -0.9672195076942444, 0.396078431372549, 0.0392156862745098, 0.058823529411764705, -0.9344390153884888, 0.49411764705882355, 0.054901960784313725, 0.03529411764705882, -0.9016585230827331, 0.5882352941176471, 0.11372549019607843, 0.023529411764705882, -0.8688780307769776, 0.6627450980392157, 0.16862745098039217, 0.01568627450980392, -0.8360975384712219, 0.7411764705882353, 0.22745098039215686, 0.00392156862745098, -0.8033170461654663, 0.788235294117647, 0.2901960784313726, 0.0, -0.7705365538597106, 0.8627450980392157, 0.3803921568627451, 0.011764705882352941, -0.7377560615539551, 0.9019607843137255, 0.4588235294117647, 0.027450980392156862, -0.7049755692481996, 0.9176470588235294, 0.5215686274509804, 0.047058823529411764, -0.6721950769424438, 0.9254901960784314, 0.5803921568627451, 0.0784313725490196, -0.6394145846366882, 0.9372549019607843, 0.6431372549019608, 0.12156862745098039, -0.6066340923309326, 0.9450980392156862, 0.7098039215686275, 0.1843137254901961, -0.573853600025177, 0.9529411764705882, 0.7686274509803922, 0.24705882352941178, -0.5410731077194214, 0.9647058823529412, 0.8274509803921568, 0.3254901960784314, -0.5082926154136658, 0.9686274509803922, 0.8784313725490196, 0.4235294117647059, -0.47551212310791013, 0.9725490196078431, 0.9176470588235294, 0.5137254901960784, -0.4427316308021545, 0.9803921568627451, 0.9490196078431372, 0.596078431372549, -0.40995113849639897, 0.9803921568627451, 0.9725490196078431, 0.6705882352941176, -0.37717064619064333, 0.9882352941176471, 0.9882352941176471, 0.7568627450980392, -0.34570137357711794, 0.984313725490196, 0.9882352941176471, 0.8549019607843137, -0.3443901538848877, 0.9882352941176471, 0.9882352941176471, 0.8588235294117647, -0.3443701538848877, 0.9529411764705882, 0.9529411764705882, 0.8941176470588236, -0.3443701538848877, 0.9529411764705882, 0.9529411764705882, 0.8941176470588236, -0.31032860028123854, 0.8901960784313725, 0.8901960784313725, 0.807843137254902, -0.2762870466775894, 0.8274509803921568, 0.8235294117647058, 0.7372549019607844, -0.24224549307394028, 0.7764705882352941, 0.7647058823529411, 0.6784313725490196, -0.20820393947029114, 0.7254901960784313, 0.7137254901960784, 0.6274509803921569, -0.174162385866642, 0.6784313725490196, 0.6627450980392157, 0.5803921568627451, -0.14012083226299288, 0.6313725490196078, 0.6078431372549019, 0.5333333333333333, -0.10607927865934375, 0.5803921568627451, 0.5568627450980392, 0.48627450980392156, -0.0720377250556945, 0.5372549019607843, 0.5058823529411764, 0.44313725490196076, -0.03799617145204537, 0.4980392156862745, 0.4588235294117647, 0.40784313725490196, -0.003954617848396236, 0.4627450980392157, 0.4196078431372549, 0.37254901960784315, 0.030086935755252897, 0.43137254901960786, 0.38823529411764707, 0.34509803921568627, 0.06412848935890203, 0.403921568627451, 0.3568627450980392, 0.3176470588235294, 0.09817004296255116, 0.37254901960784315, 0.3215686274509804, 0.29411764705882354, 0.1322115965662003, 0.34509803921568627, 0.29411764705882354, 0.26666666666666666, 0.16625315016984943, 0.3176470588235294, 0.2627450980392157, 0.23921568627450981, 0.20029470377349856, 0.28627450980392155, 0.23137254901960785, 0.21176470588235294, 0.2343362573771477, 0.2549019607843137, 0.2, 0.1843137254901961, 0.2683778109807968, 0.23137254901960785, 0.17254901960784313, 0.16470588235294117, 0.30241936458444596, 0.2, 0.1450980392156863, 0.13725490196078433, 0.3364809181880952, 0.14902, 0.196078, 0.278431, 0.4028328263692855, 0.2, 0.2549019607843137, 0.34509803921568627, 0.46918473455047605, 0.24705882352941178, 0.3176470588235294, 0.41568627450980394, 0.5355366427316666, 0.3058823529411765, 0.38823529411764707, 0.49411764705882355, 0.6018885509128571, 0.37254901960784315, 0.4588235294117647, 0.5686274509803921, 0.6682404590940476, 0.44313725490196076, 0.5333333333333333, 0.6431372549019608, 0.7345923672752379, 0.5176470588235295, 0.615686274509804, 0.7254901960784313, 0.8009442754564287, 0.6, 0.6980392156862745, 0.8, 0.867296183637619, 0.6862745098039216, 0.7843137254901961, 0.8705882352941177, 0.9336480918188095, 0.7607843137254902, 0.8588235294117647, 0.9294117647058824, 0.9668240459094049, 0.807843137254902, 0.9019607843137255, 0.9607843137254902, 1.0, 0.8901960784313725, 0.9568627450980393, 0.984313725490196]
phiLUT.ColorSpace = 'Lab'
phiLUT.NanColor = [0.0, 1.0, 0.0]
phiLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'phi'
phiPWF = GetOpacityTransferFunction('phi')
phiPWF.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
phiPWF.ScalarRangeInitialized = 1

# create a new 'Clip'
clip1 = Clip(Input=result_)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'phi']

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [62.25, 62.25, 0.0]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.0, 0.0]
clip1.ClipType.Normal = [-1.0, 1.73205080757, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'phi']
clip1Display.LookupTable = phiLUT
clip1Display.OSPRayScaleArray = 'phi'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 12.450000000000001
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.6225
clip1Display.SetScaleArray = ['POINTS', 'phi']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'phi']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = phiPWF
clip1Display.ScalarOpacityUnitDistance = 5.461513197141927

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(result_, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Reflect'
reflect1 = Reflect(Input=clip1)

# Properties modified on reflect1
reflect1.Plane = 'X'

# show data in view
reflect1Display = Show(reflect1, renderView1)

# trace defaults for the display properties.
reflect1Display.Representation = 'Surface'
reflect1Display.ColorArrayName = ['POINTS', 'phi']
reflect1Display.LookupTable = phiLUT
reflect1Display.OSPRayScaleArray = 'phi'
reflect1Display.OSPRayScaleFunction = 'PiecewiseFunction'
reflect1Display.SelectOrientationVectors = 'None'
reflect1Display.ScaleFactor = 24.900000000000002
reflect1Display.SelectScaleArray = 'None'
reflect1Display.GlyphType = 'Arrow'
reflect1Display.GlyphTableIndexArray = 'None'
reflect1Display.GaussianRadius = 1.245
reflect1Display.SetScaleArray = ['POINTS', 'phi']
reflect1Display.ScaleTransferFunction = 'PiecewiseFunction'
reflect1Display.OpacityArray = ['POINTS', 'phi']
reflect1Display.OpacityTransferFunction = 'PiecewiseFunction'
reflect1Display.DataAxesGrid = 'GridAxesRepresentation'
reflect1Display.PolarAxes = 'PolarAxesRepresentation'
reflect1Display.ScalarOpacityFunction = phiPWF
reflect1Display.ScalarOpacityUnitDistance = 7.814682406001266

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
reflect1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
reflect1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
reflect1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
reflect1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
reflect1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
reflect1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
reflect1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# hide data in view
Hide(reflect1, renderView1)

# show data in view
clip1Display = Show(clip1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# destroy reflect1
Delete(reflect1)
del reflect1

# create a new 'Reflect'
reflect1 = Reflect(Input=clip1)

# Properties modified on reflect1
reflect1.Plane = 'Y'

# show data in view
reflect1Display = Show(reflect1, renderView1)

# trace defaults for the display properties.
reflect1Display.Representation = 'Surface'
reflect1Display.ColorArrayName = ['POINTS', 'phi']
reflect1Display.LookupTable = phiLUT
reflect1Display.OSPRayScaleArray = 'phi'
reflect1Display.OSPRayScaleFunction = 'PiecewiseFunction'
reflect1Display.SelectOrientationVectors = 'None'
reflect1Display.ScaleFactor = 14.376022338867188
reflect1Display.SelectScaleArray = 'None'
reflect1Display.GlyphType = 'Arrow'
reflect1Display.GlyphTableIndexArray = 'None'
reflect1Display.GaussianRadius = 0.7188011169433594
reflect1Display.SetScaleArray = ['POINTS', 'phi']
reflect1Display.ScaleTransferFunction = 'PiecewiseFunction'
reflect1Display.OpacityArray = ['POINTS', 'phi']
reflect1Display.OpacityTransferFunction = 'PiecewiseFunction'
reflect1Display.DataAxesGrid = 'GridAxesRepresentation'
reflect1Display.PolarAxes = 'PolarAxesRepresentation'
reflect1Display.ScalarOpacityFunction = phiPWF
reflect1Display.ScalarOpacityUnitDistance = 5.7344092744672315

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
reflect1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
reflect1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
reflect1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
reflect1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
reflect1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
reflect1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
reflect1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
reflect1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# show data in view
clip1Display = Show(clip1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip1, renderView1)

# set active source
SetActiveSource(reflect1)

# create a new 'Transform'
transform1 = Transform(Input=reflect1)
transform1.Transform = 'Transform'

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, 0.0, 60.0]

# show data in view
transform1Display = Show(transform1, renderView1)

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = ['POINTS', 'phi']
transform1Display.LookupTable = phiLUT
transform1Display.OSPRayScaleArray = 'phi'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'None'
transform1Display.ScaleFactor = 14.376022338867188
transform1Display.SelectScaleArray = 'None'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'None'
transform1Display.GaussianRadius = 0.7188011169433594
transform1Display.SetScaleArray = ['POINTS', 'phi']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'phi']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.PolarAxes = 'PolarAxesRepresentation'
transform1Display.ScalarOpacityFunction = phiPWF
transform1Display.ScalarOpacityUnitDistance = 5.7344093347256475

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
transform1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
transform1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
transform1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
transform1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
transform1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
transform1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
transform1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
transform1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
transform1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
transform1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Transform'
transform2 = Transform(Input=transform1)
transform2.Transform = 'Transform'

# Properties modified on transform2.Transform
transform2.Transform.Rotate = [0.0, 0.0, 60.0]

# show data in view
transform2Display = Show(transform2, renderView1)

# trace defaults for the display properties.
transform2Display.Representation = 'Surface'
transform2Display.ColorArrayName = ['POINTS', 'phi']
transform2Display.LookupTable = phiLUT
transform2Display.OSPRayScaleArray = 'phi'
transform2Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform2Display.SelectOrientationVectors = 'None'
transform2Display.ScaleFactor = 14.376020812988282
transform2Display.SelectScaleArray = 'None'
transform2Display.GlyphType = 'Arrow'
transform2Display.GlyphTableIndexArray = 'None'
transform2Display.GaussianRadius = 0.7188010406494141
transform2Display.SetScaleArray = ['POINTS', 'phi']
transform2Display.ScaleTransferFunction = 'PiecewiseFunction'
transform2Display.OpacityArray = ['POINTS', 'phi']
transform2Display.OpacityTransferFunction = 'PiecewiseFunction'
transform2Display.DataAxesGrid = 'GridAxesRepresentation'
transform2Display.PolarAxes = 'PolarAxesRepresentation'
transform2Display.ScalarOpacityFunction = phiPWF
transform2Display.ScalarOpacityUnitDistance = 5.734409159308398

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform2Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform2Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
transform2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
transform2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
transform2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
transform2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
transform2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
transform2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
transform2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
transform2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
transform2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
transform2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(transform1, renderView1)

# show color bar/color legend
transform2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform1)

# show data in view
transform1Display = Show(transform1, renderView1)

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display = Show(reflect1, renderView1)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Transform'
transform3 = Transform(Input=reflect1)
transform3.Transform = 'Transform'

# Properties modified on transform3.Transform
transform3.Transform.Rotate = [0.0, 0.0, -60.0]

# show data in view
transform3Display = Show(transform3, renderView1)

# trace defaults for the display properties.
transform3Display.Representation = 'Surface'
transform3Display.ColorArrayName = ['POINTS', 'phi']
transform3Display.LookupTable = phiLUT
transform3Display.OSPRayScaleArray = 'phi'
transform3Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform3Display.SelectOrientationVectors = 'None'
transform3Display.ScaleFactor = 14.376022338867188
transform3Display.SelectScaleArray = 'None'
transform3Display.GlyphType = 'Arrow'
transform3Display.GlyphTableIndexArray = 'None'
transform3Display.GaussianRadius = 0.7188011169433594
transform3Display.SetScaleArray = ['POINTS', 'phi']
transform3Display.ScaleTransferFunction = 'PiecewiseFunction'
transform3Display.OpacityArray = ['POINTS', 'phi']
transform3Display.OpacityTransferFunction = 'PiecewiseFunction'
transform3Display.DataAxesGrid = 'GridAxesRepresentation'
transform3Display.PolarAxes = 'PolarAxesRepresentation'
transform3Display.ScalarOpacityFunction = phiPWF
transform3Display.ScalarOpacityUnitDistance = 5.7344093347256475

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform3Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform3Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
transform3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
transform3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
transform3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
transform3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
transform3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
transform3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
transform3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
transform3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
transform3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
transform3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
transform3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Transform'
transform4 = Transform(Input=transform3)
transform4.Transform = 'Transform'

# Properties modified on transform4.Transform
transform4.Transform.Rotate = [0.0, 0.0, -60.0]

# show data in view
transform4Display = Show(transform4, renderView1)

# trace defaults for the display properties.
transform4Display.Representation = 'Surface'
transform4Display.ColorArrayName = ['POINTS', 'phi']
transform4Display.LookupTable = phiLUT
transform4Display.OSPRayScaleArray = 'phi'
transform4Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform4Display.SelectOrientationVectors = 'None'
transform4Display.ScaleFactor = 14.376020812988282
transform4Display.SelectScaleArray = 'None'
transform4Display.GlyphType = 'Arrow'
transform4Display.GlyphTableIndexArray = 'None'
transform4Display.GaussianRadius = 0.7188010406494141
transform4Display.SetScaleArray = ['POINTS', 'phi']
transform4Display.ScaleTransferFunction = 'PiecewiseFunction'
transform4Display.OpacityArray = ['POINTS', 'phi']
transform4Display.OpacityTransferFunction = 'PiecewiseFunction'
transform4Display.DataAxesGrid = 'GridAxesRepresentation'
transform4Display.PolarAxes = 'PolarAxesRepresentation'
transform4Display.ScalarOpacityFunction = phiPWF
transform4Display.ScalarOpacityUnitDistance = 5.734409159308398

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform4Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform4Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
transform4Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
transform4Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
transform4Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
transform4Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
transform4Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
transform4Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
transform4Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
transform4Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
transform4Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
transform4Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(transform3, renderView1)

# show color bar/color legend
transform4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(transform3)

# show data in view
transform3Display = Show(transform3, renderView1)

# show color bar/color legend
transform3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display = Show(reflect1, renderView1)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Transform'
transform5 = Transform(Input=reflect1)
transform5.Transform = 'Transform'

# Properties modified on transform5.Transform
transform5.Transform.Rotate = [0.0, 0.0, -180.0]

# show data in view
transform5Display = Show(transform5, renderView1)

# trace defaults for the display properties.
transform5Display.Representation = 'Surface'
transform5Display.ColorArrayName = ['POINTS', 'phi']
transform5Display.LookupTable = phiLUT
transform5Display.OSPRayScaleArray = 'phi'
transform5Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform5Display.SelectOrientationVectors = 'None'
transform5Display.ScaleFactor = 14.376022338867188
transform5Display.SelectScaleArray = 'None'
transform5Display.GlyphType = 'Arrow'
transform5Display.GlyphTableIndexArray = 'None'
transform5Display.GaussianRadius = 0.7188011169433594
transform5Display.SetScaleArray = ['POINTS', 'phi']
transform5Display.ScaleTransferFunction = 'PiecewiseFunction'
transform5Display.OpacityArray = ['POINTS', 'phi']
transform5Display.OpacityTransferFunction = 'PiecewiseFunction'
transform5Display.DataAxesGrid = 'GridAxesRepresentation'
transform5Display.PolarAxes = 'PolarAxesRepresentation'
transform5Display.ScalarOpacityFunction = phiPWF
transform5Display.ScalarOpacityUnitDistance = 5.7344092744672315

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform5Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform5Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
transform5Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
transform5Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
transform5Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
transform5Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
transform5Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
transform5Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
transform5Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
transform5Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
transform5Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
transform5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
transform5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display = Show(reflect1, renderView1)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 124.5, -71.88011169433594, 71.88011169433594, 0.0, 0.0)

#change interaction mode for render view
renderView1.InteractionMode = '3D'

# get the material library
materialLibrary1 = GetMaterialLibrary()

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=reflect1)
warpByScalar1.Scalars = ['POINTS', 'phi']

# show data in view
warpByScalar1Display = Show(warpByScalar1, renderView1)

# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.ColorArrayName = ['POINTS', 'phi']
warpByScalar1Display.LookupTable = phiLUT
warpByScalar1Display.OSPRayScaleArray = 'phi'
warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByScalar1Display.SelectOrientationVectors = 'None'
warpByScalar1Display.ScaleFactor = 14.376022338867188
warpByScalar1Display.SelectScaleArray = 'None'
warpByScalar1Display.GlyphType = 'Arrow'
warpByScalar1Display.GlyphTableIndexArray = 'None'
warpByScalar1Display.GaussianRadius = 0.7188011169433594
warpByScalar1Display.SetScaleArray = ['POINTS', 'phi']
warpByScalar1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.OpacityArray = ['POINTS', 'phi']
warpByScalar1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
warpByScalar1Display.ScalarOpacityFunction = phiPWF
warpByScalar1Display.ScalarOpacityUnitDistance = 5.7347263707596365

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
warpByScalar1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
warpByScalar1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
warpByScalar1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
warpByScalar1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
warpByScalar1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
warpByScalar1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
warpByScalar1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
warpByScalar1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(reflect1)

# hide data in view
Hide(warpByScalar1, renderView1)

# show data in view
reflect1Display = Show(reflect1, renderView1)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# destroy warpByScalar1
Delete(warpByScalar1)
del warpByScalar1

# set active source
SetActiveSource(reflect1)

# set active source
SetActiveSource(transform5)

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(Input=[reflect1, transform1, transform2, transform3, transform4, transform5])

# show data in view
groupDatasets1Display = Show(groupDatasets1, renderView1)

# trace defaults for the display properties.
groupDatasets1Display.Representation = 'Surface'
groupDatasets1Display.ColorArrayName = ['POINTS', 'phi']
groupDatasets1Display.LookupTable = phiLUT
groupDatasets1Display.OSPRayScaleArray = 'phi'
groupDatasets1Display.OSPRayScaleFunction = 'PiecewiseFunction'
groupDatasets1Display.SelectOrientationVectors = 'None'
groupDatasets1Display.ScaleFactor = 28.752044677734375
groupDatasets1Display.SelectScaleArray = 'None'
groupDatasets1Display.GlyphType = 'Arrow'
groupDatasets1Display.GlyphTableIndexArray = 'None'
groupDatasets1Display.GaussianRadius = 1.4376022338867187
groupDatasets1Display.SetScaleArray = ['POINTS', 'phi']
groupDatasets1Display.ScaleTransferFunction = 'PiecewiseFunction'
groupDatasets1Display.OpacityArray = ['POINTS', 'phi']
groupDatasets1Display.OpacityTransferFunction = 'PiecewiseFunction'
groupDatasets1Display.DataAxesGrid = 'GridAxesRepresentation'
groupDatasets1Display.PolarAxes = 'PolarAxesRepresentation'
groupDatasets1Display.ScalarOpacityFunction = phiPWF
groupDatasets1Display.ScalarOpacityUnitDistance = 6.311534162772303
groupDatasets1Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
groupDatasets1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
groupDatasets1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
groupDatasets1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
groupDatasets1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
groupDatasets1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
groupDatasets1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
groupDatasets1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(reflect1, renderView1)

# hide data in view
Hide(transform5, renderView1)

# hide data in view
Hide(transform1, renderView1)

# hide data in view
Hide(transform3, renderView1)

# hide data in view
Hide(transform4, renderView1)

# hide data in view
Hide(transform2, renderView1)

# show color bar/color legend
groupDatasets1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=groupDatasets1)
warpByScalar1.Scalars = ['POINTS', 'phi']

# Properties modified on warpByScalar1
warpByScalar1.ScaleFactor = 2.0

# show data in view
warpByScalar1Display = Show(warpByScalar1, renderView1)

# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.ColorArrayName = ['POINTS', 'phi']
warpByScalar1Display.LookupTable = phiLUT
warpByScalar1Display.OSPRayScaleArray = 'phi'
warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByScalar1Display.SelectOrientationVectors = 'None'
warpByScalar1Display.ScaleFactor = 28.752044677734375
warpByScalar1Display.SelectScaleArray = 'None'
warpByScalar1Display.GlyphType = 'Arrow'
warpByScalar1Display.GlyphTableIndexArray = 'None'
warpByScalar1Display.GaussianRadius = 1.4376022338867187
warpByScalar1Display.SetScaleArray = ['POINTS', 'phi']
warpByScalar1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.OpacityArray = ['POINTS', 'phi']
warpByScalar1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
warpByScalar1Display.ScalarOpacityFunction = phiPWF
warpByScalar1Display.ScalarOpacityUnitDistance = 6.311883172397194
warpByScalar1Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
warpByScalar1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
warpByScalar1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
warpByScalar1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
warpByScalar1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
warpByScalar1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
warpByScalar1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
warpByScalar1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(groupDatasets1, renderView1)

# show color bar/color legend
warpByScalar1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [139.2397018119569, -123.16344363375126, 344.12634377147214]
renderView1.CameraFocalPoint = [0.20858796305933053, -14.727718247098652, 21.806527072468416]
renderView1.CameraViewUp = [-0.07969859332758371, 0.9338918548648468, 0.3485600918617912]
renderView1.CameraParallelScale = 168.45498615906087

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).