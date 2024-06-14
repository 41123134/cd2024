# NX 1872
# Journal created by Admin on Fri Jun 14 14:40:27 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Drawings
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder1.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId1, "建立草圖 對話方塊")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject1 = sketchInPlaceBuilder1.Commit()
    
    sketch1 = nXObject1
    feature1 = sketch1.Feature
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId4)
    
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "建立草圖")
    
    sketchInPlaceBuilder1.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane1.DestroyPlane()
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->矩形(R)...
    # ----------------------------------------------
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId6, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    endPoint1 = NXOpen.Point3d(59.0, 0.0, 0.0)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    startPoint2 = NXOpen.Point3d(59.0, 0.0, 0.0)
    endPoint2 = NXOpen.Point3d(59.0, 58.0, 0.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    startPoint3 = NXOpen.Point3d(59.0, 58.0, 0.0)
    endPoint3 = NXOpen.Point3d(0.0, 58.0, 0.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(0.0, 58.0, 0.0)
    endPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)
    
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = line1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_1.Geometry = line2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_2.Geometry = line2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_2.SplineDefiningPointIndex = 0
    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_2.Geometry = line3
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)
    
    geom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_3.Geometry = line3
    geom1_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_3.SplineDefiningPointIndex = 0
    geom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_3.Geometry = line4
    geom2_3.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_3, geom2_3)
    
    geom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_4.Geometry = line4
    geom1_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_4.SplineDefiningPointIndex = 0
    geom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_4.Geometry = line1
    geom2_4.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_4, geom2_4)
    
    geom1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1.Geometry = line1
    geom1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateHorizontalConstraint(geom1)
    
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint6 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)
    
    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_2.Geometry = line2
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_2.SplineDefiningPointIndex = 0
    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_2.Geometry = line3
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint7 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)
    
    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_3.Geometry = line3
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_3.SplineDefiningPointIndex = 0
    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_3.Geometry = line4
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint8 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)
    
    conGeom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_4.Geometry = line4
    conGeom1_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_4.SplineDefiningPointIndex = 0
    conGeom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_4.Geometry = line1
    conGeom2_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint9 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = line1
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys1 = workPart.Features.FindObject("SKETCH(1:1B)")
    point1 = datumCsys1.FindObject("POINT 1")
    geom2_5.Geometry = point1
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)
    
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_1.Geometry = line1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null
    dimObject2_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_1.Geometry = line1
    dimObject2_1.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_1.AssocValue = 0
    dimObject2_1.HelpPoint.X = 0.0
    dimObject2_1.HelpPoint.Y = 0.0
    dimObject2_1.HelpPoint.Z = 0.0
    dimObject2_1.View = NXOpen.NXObject.Null
    dimOrigin1 = NXOpen.Point3d(29.5, -10.03422962062071, 0.0)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint1 = sketchDimensionalConstraint1
    dimension1 = sketchHelpedDimensionalConstraint1.AssociatedDimension
    
    expression3 = sketchHelpedDimensionalConstraint1.AssociatedExpression
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = line2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimObject2_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_2.Geometry = line2
    dimObject2_2.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_2.AssocValue = 0
    dimObject2_2.HelpPoint.X = 0.0
    dimObject2_2.HelpPoint.Y = 0.0
    dimObject2_2.HelpPoint.Z = 0.0
    dimObject2_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(69.034229620620707, 29.0, 0.0)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint2 = sketchDimensionalConstraint2
    dimension2 = sketchHelpedDimensionalConstraint2.AssociatedDimension
    
    expression4 = sketchHelpedDimensionalConstraint2.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms1 = [NXOpen.SmartObject.Null] * 4 
    geoms1[0] = line1
    geoms1[1] = line2
    geoms1[2] = line3
    geoms1[3] = line4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)
    
    geoms2 = [NXOpen.SmartObject.Null] * 4 
    geoms2[0] = line1
    geoms2[1] = line2
    geoms2[2] = line3
    geoms2[3] = line4
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms2)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖約束(K)->尺寸(D)->快速(P)...
    # ----------------------------------------------
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder1 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines1 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines1)
    
    lines2 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines2)
    
    lines3 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines3)
    
    lines4 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines4)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines5 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines5)
    
    lines6 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines6)
    
    lines7 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines7)
    
    lines8 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines8)
    
    theSession.SetUndoMarkName(markId7, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits1 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits2 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits3 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits4 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits5 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits6 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits7 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits8 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits9 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits10 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits11 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits12 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits13 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits14 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits15 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits16 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits17 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits18 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits19 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits20 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    point2 = NXOpen.Point3d(59.0, 33.628605659108018, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(line2, workPart.ModelingViews.WorkView, point2)
    
    point1_1 = NXOpen.Point3d(59.0, 58.0, 0.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line2, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(59.0, 0.0, 0.0)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line2, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
    dimensionlinearunits21 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits22 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits23 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits24 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits25 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits26 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin1 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin1.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin1.View = NXOpen.View.Null
    assocOrigin1.ViewOfGeometry = workPart.ModelingViews.WorkView
    point3 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin1.PointOnGeometry = point3
    assocOrigin1.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.DimensionLine = 0
    assocOrigin1.AssociatedView = NXOpen.View.Null
    assocOrigin1.AssociatedPoint = NXOpen.Point.Null
    assocOrigin1.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.XOffsetFactor = 0.0
    assocOrigin1.YOffsetFactor = 0.0
    assocOrigin1.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder1.Origin.SetAssociativeOrigin(assocOrigin1)
    
    point4 = NXOpen.Point3d(82.891563072011834, 30.678727969712586, 0.0)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point4)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = True
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject2 = sketchRapidDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId8, None)
    
    theSession.SetUndoMarkName(markId7, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId7, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder2 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines9 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBefore(lines9)
    
    lines10 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAfter(lines10)
    
    lines11 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAbove(lines11)
    
    lines12 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBelow(lines12)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder2.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId9, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder2.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits27 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits28 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits29 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits30 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits31 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits32 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits33 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits34 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits35 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits36 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder2.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits37 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits38 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits39 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits40 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits41 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits42 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits43 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits44 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits45 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits46 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    expression5 = workPart.Expressions.FindObject("p6")
    expression5.SetFormula("200")
    
    theSession.SetUndoMarkVisibility(markId9, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.Scale(3.4482758620689653)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId10, None)
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId9, "Edit Driving Value")
    
    point5 = NXOpen.Point3d(50.44290848866202, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(line1, workPart.ModelingViews.WorkView, point5)
    
    point1_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line1, workPart.ModelingViews.WorkView, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
    point1_4 = NXOpen.Point3d(203.44827586206895, 0.0, 0.0)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line1, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    dimensionlinearunits47 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits48 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits49 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits50 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits51 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits52 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin2 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin2.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin2.View = NXOpen.View.Null
    assocOrigin2.ViewOfGeometry = workPart.ModelingViews.WorkView
    point6 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin2.PointOnGeometry = point6
    assocOrigin2.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.DimensionLine = 0
    assocOrigin2.AssociatedView = NXOpen.View.Null
    assocOrigin2.AssociatedPoint = NXOpen.Point.Null
    assocOrigin2.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.XOffsetFactor = 0.0
    assocOrigin2.YOffsetFactor = 0.0
    assocOrigin2.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder2.Origin.SetAssociativeOrigin(assocOrigin2)
    
    point7 = NXOpen.Point3d(48.967969643964288, -16.51931506061446, 0.0)
    sketchRapidDimensionBuilder2.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point7)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.TextCentered = False
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject3 = sketchRapidDimensionBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId12, None)
    
    theSession.SetUndoMarkName(markId11, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId11, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder3 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines13 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBefore(lines13)
    
    lines14 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAfter(lines14)
    
    lines15 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAbove(lines15)
    
    lines16 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBelow(lines16)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder3.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId13, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder3.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits53 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits54 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits55 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits56 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits57 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits58 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits59 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits60 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits61 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits62 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder3.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits63 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits64 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits65 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits66 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits67 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits68 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits69 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits70 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits71 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits72 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    expression6 = workPart.Expressions.FindObject("p7")
    expression6.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId13, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId14, None)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId13, "Edit Driving Value")
    
    expression6.SetFormula("200")
    
    theSession.SetUndoMarkVisibility(markId15, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId16, None)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId15, "Edit Driving Value")
    
    sketchRapidDimensionBuilder3.Destroy()
    
    theSession.UndoToMark(markId17, None)
    
    theSession.DeleteUndoMark(markId17, None)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    sketch2 = theSession.ActiveSketch
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("30")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId19, "拉伸 對話方塊")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(68.138394209846695, 0.0, 3.5527136788005009e-15)
    section1.AddToSection(rules1, line1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId21, None)
    
    direction1 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction1
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId20, None)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("100")
    
    scaleAboutPoint1 = NXOpen.Point3d(44.2481653409316, -20.944131594707617, 0.0)
    viewCenter1 = NXOpen.Point3d(-44.2481653409316, 20.944131594707617, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(35.398532272745278, -16.755305275766094, 0.0)
    viewCenter2 = NXOpen.Point3d(-35.398532272745278, 16.755305275766094, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(28.318825818196224, -13.404244220612874, 0.0)
    viewCenter3 = NXOpen.Point3d(-28.318825818196224, 13.404244220612874, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(22.504026916859932, -10.57236163879325, 0.0)
    viewCenter4 = NXOpen.Point3d(-22.504026916859932, 10.57236163879325, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(28.130033646074896, -13.21545204849156, 0.0)
    viewCenter5 = NXOpen.Point3d(-28.130033646074896, 13.21545204849156, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(35.162542057593626, -16.519315060614453, 0.0)
    viewCenter6 = NXOpen.Point3d(-35.162542057593626, 16.519315060614453, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(43.953177571992029, -20.649143825768064, 0.0)
    viewCenter7 = NXOpen.Point3d(-43.953177571992029, 20.649143825768039, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(54.9414719649901, -25.811429782210116, 0.0)
    viewCenter8 = NXOpen.Point3d(-54.941471964990036, 25.811429782210052, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(68.215921567269532, -32.264287227762644, 0.0)
    viewCenter9 = NXOpen.Point3d(-68.215921567269532, 32.264287227762566, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint9, viewCenter9)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.068001523680365078
    rotMatrix1.Xy = 0.97603321825634071
    rotMatrix1.Xz = -0.20672433247520972
    rotMatrix1.Yx = -0.10159511758543251
    rotMatrix1.Yy = 0.2129012338398007
    rotMatrix1.Yz = 0.9717774934172394
    rotMatrix1.Zx = 0.99249897977778889
    rotMatrix1.Zy = -0.045080167365068848
    rotMatrix1.Zz = 0.11363781787057725
    translation1 = NXOpen.Point3d(99.189155471971659, -41.513362422492371, -66.187323701852279)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.45922807970533103)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("150")
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId22, None)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId23, None)
    
    theSession.SetUndoMarkName(markId19, "拉伸")
    
    expression9 = extrudeBuilder1.Limits.StartExtend.Value
    expression10 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression7)
    
    workPart.Expressions.Delete(expression8)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = -0.19689725988821249
    rotMatrix2.Xy = 0.93347930546507674
    rotMatrix2.Xz = -0.29974631827089154
    rotMatrix2.Yx = -0.24178220113021251
    rotMatrix2.Yy = 0.25005693003275664
    rotMatrix2.Yz = 0.93755687771954577
    rotMatrix2.Zx = 0.95014358718308778
    rotMatrix2.Zy = 0.25707570482454023
    rotMatrix2.Zz = 0.17646315684533995
    translation2 = NXOpen.Point3d(136.91107404263198, -28.643677509982929, -96.879272084450278)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.45922807970533103)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.PlaneReference = plane2
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder2 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder2.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId24, "建立草圖 對話方塊")
    
    scalar1 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrude1 = feature2
    edge1 = extrude1.FindObject("EDGE * 120 * 150 {(200,-0,0)(200,100,0)(200,200,0) EXTRUDE(2)}")
    point8 = workPart.Points.CreatePoint(edge1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction2 = workPart.Directions.CreateDirection(edge1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face1 = extrude1.FindObject("FACE 150 {(200,100,75) EXTRUDE(2)}")
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction2, point8, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem1
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane3 = workPart.Planes.CreatePlane(origin3, normal3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane3.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom2 = [NXOpen.NXObject.Null] * 1 
    geom2[0] = face1
    plane3.SetGeometry(geom2)
    
    plane3.SetFlip(False)
    
    plane3.SetExpression(None)
    
    plane3.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane3.Evaluate()
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane4.SynchronizeToPlane(plane3)
    
    scalar2 = workPart.Scalars.CreateScalar(100.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point9 = workPart.Points.CreatePoint(edge1, scalar2, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane4.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom3 = [NXOpen.NXObject.Null] * 1 
    geom3[0] = face1
    plane4.SetGeometry(geom3)
    
    plane4.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane4.Evaluate()
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId25, None)
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject4 = sketchInPlaceBuilder2.Commit()
    
    sketch3 = nXObject4
    feature3 = sketch3.Feature
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId27)
    
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId26, None)
    
    theSession.SetUndoMarkName(markId24, "建立草圖")
    
    sketchInPlaceBuilder2.Destroy()
    
    sketchAlongPathBuilder2.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression12)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point9)
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression11)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane2.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression14)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression13)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane4.DestroyPlane()
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->圓(C)...
    # ----------------------------------------------
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId29, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(199.99999999999997, 175.00000000000003, 25.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 16.092374736873683, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = arc1
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = 0.0
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = 0.0
    dimObject1_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(199.99999999999997, 175.00000000000003, 31.532701575924943)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_3, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension3 = sketchDimensionalConstraint3.AssociatedDimension
    
    expression15 = sketchDimensionalConstraint3.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId30, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(199.99999999999997, 25.427160178355734, 25.0)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 19.2543620204242, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_4.Geometry = arc2
    dimObject1_4.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_4.AssocValue = 0
    dimObject1_4.HelpPoint.X = 0.0
    dimObject1_4.HelpPoint.Y = 0.0
    dimObject1_4.HelpPoint.Z = 0.0
    dimObject1_4.View = NXOpen.NXObject.Null
    dimOrigin4 = NXOpen.Point3d(199.99999999999997, 25.427160178355734, 31.532701575924943)
    sketchDimensionalConstraint4 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_4, dimOrigin4, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension4 = sketchDimensionalConstraint4.AssociatedDimension
    
    expression16 = sketchDimensionalConstraint4.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->草圖約束(K)->尺寸(D)->快速(P)...
    # ----------------------------------------------
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder4 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines17 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines17)
    
    lines18 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines18)
    
    lines19 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines19)
    
    lines20 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines20)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder4.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines21 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines21)
    
    lines22 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines22)
    
    lines23 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines23)
    
    lines24 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines24)
    
    theSession.SetUndoMarkName(markId31, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder4.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits73 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits74 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits75 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits76 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits77 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits78 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits79 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits80 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits81 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits82 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder4.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits83 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits84 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits85 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits86 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits87 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits88 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits89 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits90 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits91 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits92 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) Z axis")
    point10 = NXOpen.Point3d(0.0, 0.0, 30.535843269132442)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(datumAxis1, workPart.ModelingViews.WorkView, point10)
    
    point1_5 = NXOpen.Point3d(199.99999999999997, 25.427160178355734, 25.0)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    dimensionlinearunits93 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits94 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits95 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits96 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits97 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits98 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin3 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin3.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin3.View = NXOpen.View.Null
    assocOrigin3.ViewOfGeometry = workPart.ModelingViews.WorkView
    point11 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin3.PointOnGeometry = point11
    assocOrigin3.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.DimensionLine = 0
    assocOrigin3.AssociatedView = NXOpen.View.Null
    assocOrigin3.AssociatedPoint = NXOpen.Point.Null
    assocOrigin3.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.XOffsetFactor = 0.0
    assocOrigin3.YOffsetFactor = 0.0
    assocOrigin3.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder4.Origin.SetAssociativeOrigin(assocOrigin3)
    
    point12 = NXOpen.Point3d(199.99999999999997, 17.361088371415065, 69.137758345205583)
    sketchRapidDimensionBuilder4.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point12)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.TextCentered = False
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject5 = sketchRapidDimensionBuilder4.Commit()
    
    theSession.DeleteUndoMark(markId32, None)
    
    theSession.SetUndoMarkName(markId31, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId31, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder5 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines25 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBefore(lines25)
    
    lines26 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAfter(lines26)
    
    lines27 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAbove(lines27)
    
    lines28 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBelow(lines28)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder5.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId33, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder5.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits99 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits100 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits101 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits102 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits103 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits104 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits105 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits106 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits107 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits108 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder5.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits109 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits110 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits111 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits112 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits113 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits114 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits115 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits116 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits117 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits118 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    expression17 = workPart.Expressions.FindObject("p10")
    expression17.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId33, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId34, None)
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId33, "Edit Driving Value")
    
    expression17.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId35, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId36, None)
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId35, "Edit Driving Value")
    
    sketchRapidDimensionBuilder5.Destroy()
    
    theSession.UndoToMark(markId37, None)
    
    theSession.DeleteUndoMark(markId37, None)
    
    sketchRapidDimensionBuilder5.Destroy()
    
    scaleAboutPoint10 = NXOpen.Point3d(-194.738019338996, 78.356126124566345, 0.0)
    viewCenter10 = NXOpen.Point3d(194.7380193389958, -78.356126124566401, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-243.42252417374496, 97.945157655707987, 0.0)
    viewCenter11 = NXOpen.Point3d(243.42252417374473, -97.945157655707987, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-304.27815521718122, 122.43144706963506, 0.0)
    viewCenter12 = NXOpen.Point3d(304.27815521718088, -122.4314470696349, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-344.3384448833483, 118.15534873448226, 0.0)
    viewCenter13 = NXOpen.Point3d(344.3384448833483, -118.15534873448226, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-275.47075590667879, 94.524278987585816, 0.0)
    viewCenter14 = NXOpen.Point3d(275.47075590667851, -94.524278987585816, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(-220.37660472534304, 75.619423190068659, 0.0)
    viewCenter15 = NXOpen.Point3d(220.37660472534282, -75.619423190068659, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-176.30128378027445, 60.495538552054924, 0.0)
    viewCenter16 = NXOpen.Point3d(176.30128378027422, -60.495538552054924, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-150.25939480358042, 55.310206676164498, 0.0)
    viewCenter17 = NXOpen.Point3d(150.25939480358016, -55.310206676164498, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(-120.20751584286432, 44.248165340931564, 0.0)
    viewCenter18 = NXOpen.Point3d(120.20751584286407, -44.248165340931628, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(-96.166012674291466, 35.398532272745257, 0.0)
    viewCenter19 = NXOpen.Point3d(96.166012674291238, -35.398532272745307, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(-76.932810139433172, 28.318825818196185, 0.0)
    viewCenter20 = NXOpen.Point3d(76.932810139432988, -28.318825818196224, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(-61.546248111546568, 22.843852826678276, 0.0)
    viewCenter21 = NXOpen.Point3d(61.546248111546376, -22.843852826678308, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    perpendicularDimension1 = nXObject5
    objects1[0] = perpendicularDimension1
    nErrs3 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs4 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId38, None)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖約束(K)->尺寸(D)->快速(P)...
    # ----------------------------------------------
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder6 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines29 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines29)
    
    lines30 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines30)
    
    lines31 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines31)
    
    lines32 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines32)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder6.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines33 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines33)
    
    lines34 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines34)
    
    lines35 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines35)
    
    lines36 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines36)
    
    theSession.SetUndoMarkName(markId40, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder6.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits119 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits120 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits121 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits122 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits123 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits124 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits125 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits126 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits127 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits128 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder6.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits129 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits130 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits131 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits132 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits133 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits134 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits135 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits136 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits137 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits138 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    edge2 = extrude1.FindObject("EDGE * 140 * 150 {(200,-0,150)(200,-0,75)(200,-0,0) EXTRUDE(2)}")
    point13 = NXOpen.Point3d(200.00000000000003, -9.8607613152626476e-32, 80.630447830359046)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(edge2, workPart.ModelingViews.WorkView, point13)
    
    point1_6 = NXOpen.Point3d(199.99999999999997, 20.0, 25.0)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    dimensionlinearunits139 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits140 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits141 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits142 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits143 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits144 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin4 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin4.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin4.View = NXOpen.View.Null
    assocOrigin4.ViewOfGeometry = workPart.ModelingViews.WorkView
    point14 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin4.PointOnGeometry = point14
    assocOrigin4.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.DimensionLine = 0
    assocOrigin4.AssociatedView = NXOpen.View.Null
    assocOrigin4.AssociatedPoint = NXOpen.Point.Null
    assocOrigin4.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.XOffsetFactor = 0.0
    assocOrigin4.YOffsetFactor = 0.0
    assocOrigin4.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder6.Origin.SetAssociativeOrigin(assocOrigin4)
    
    point15 = NXOpen.Point3d(199.99999999999997, 10.908138742184619, 59.183657077378427)
    sketchRapidDimensionBuilder6.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point15)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.TextCentered = True
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject6 = sketchRapidDimensionBuilder6.Commit()
    
    theSession.DeleteUndoMark(markId41, None)
    
    theSession.SetUndoMarkName(markId40, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId40, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder6.Destroy()
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder7 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines37 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBefore(lines37)
    
    lines38 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAfter(lines38)
    
    lines39 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAbove(lines39)
    
    lines40 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBelow(lines40)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder7.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId42, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder7.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits145 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits146 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits147 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits148 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits149 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits150 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits151 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits152 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits153 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits154 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder7.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits155 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits156 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits157 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits158 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits159 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits160 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits161 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits162 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits163 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits164 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    point16 = NXOpen.Point3d(200.00000000000003, 22.990837757948327, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(line2, workPart.ModelingViews.WorkView, point16)
    
    point1_7 = NXOpen.Point3d(199.99999999999997, 20.0, 25.0)
    point2_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_7, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_7)
    
    dimensionlinearunits165 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits166 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits167 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits168 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits169 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits170 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin5 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin5.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin5.View = NXOpen.View.Null
    assocOrigin5.ViewOfGeometry = workPart.ModelingViews.WorkView
    point17 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin5.PointOnGeometry = point17
    assocOrigin5.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.DimensionLine = 0
    assocOrigin5.AssociatedView = NXOpen.View.Null
    assocOrigin5.AssociatedPoint = NXOpen.Point.Null
    assocOrigin5.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.XOffsetFactor = 0.0
    assocOrigin5.YOffsetFactor = 0.0
    assocOrigin5.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder7.Origin.SetAssociativeOrigin(assocOrigin5)
    
    point18 = NXOpen.Point3d(199.99999999999997, 56.973428739783799, 14.628704456749698)
    sketchRapidDimensionBuilder7.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point18)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.TextCentered = True
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject7 = sketchRapidDimensionBuilder7.Commit()
    
    theSession.DeleteUndoMark(markId43, None)
    
    theSession.SetUndoMarkName(markId42, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId42, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder7.Destroy()
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder8 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines41 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBefore(lines41)
    
    lines42 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAfter(lines42)
    
    lines43 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAbove(lines43)
    
    lines44 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBelow(lines44)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder8.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId44, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder8.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits171 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits172 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits173 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits174 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits175 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits176 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits177 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits178 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits179 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits180 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder8.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits181 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits182 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits183 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits184 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits185 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits186 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits187 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits188 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits189 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits190 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    expression18 = workPart.Expressions.FindObject("p11")
    expression18.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId44, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId45, None)
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId44, "Edit Driving Value")
    
    point1_8 = NXOpen.Point3d(199.99999999999997, 37.767986888047872, 27.418160065657293)
    point2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_8, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_8)
    
    point1_9 = NXOpen.Point3d(199.99999999999997, 37.767986888047872, 27.418160065657293)
    point2_9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_9, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_9)
    
    point1_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_10, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_10)
    
    dimensionlinearunits191 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits192 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits193 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits194 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits195 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits196 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin6 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin6.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin6.View = NXOpen.View.Null
    assocOrigin6.ViewOfGeometry = workPart.ModelingViews.WorkView
    point19 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin6.PointOnGeometry = point19
    assocOrigin6.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.DimensionLine = 0
    assocOrigin6.AssociatedView = NXOpen.View.Null
    assocOrigin6.AssociatedPoint = NXOpen.Point.Null
    assocOrigin6.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.XOffsetFactor = 0.0
    assocOrigin6.YOffsetFactor = 0.0
    assocOrigin6.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder8.Origin.SetAssociativeOrigin(assocOrigin6)
    
    point20 = NXOpen.Point3d(199.99999999999997, 55.765158838207434, 40.002372389853512)
    sketchRapidDimensionBuilder8.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point20)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.TextCentered = False
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject8 = sketchRapidDimensionBuilder8.Commit()
    
    theSession.DeleteUndoMark(markId47, None)
    
    theSession.SetUndoMarkName(markId46, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId46, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder8.Destroy()
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder9 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines45 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBefore(lines45)
    
    lines46 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAfter(lines46)
    
    lines47 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAbove(lines47)
    
    lines48 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBelow(lines48)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder9.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId48, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder9.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits197 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits198 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits199 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits200 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits201 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits202 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits203 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits204 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits205 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits206 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder9.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits207 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits208 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits209 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits210 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits211 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits212 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits213 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits214 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits215 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits216 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    expression19 = workPart.Expressions.FindObject("p12")
    expression19.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId48, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId49, None)
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId48, "Edit Driving Value")
    
    scaleAboutPoint22 = NXOpen.Point3d(6.7965181963670167, -17.821981048251494, 0.0)
    viewCenter22 = NXOpen.Point3d(-6.7965181963671712, 17.82198104825147, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(8.6844399175801001, -22.843852826678308, 0.0)
    viewCenter23 = NXOpen.Point3d(-8.6844399175802298, 22.843852826678244, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint23, viewCenter23)
    
    point1_11 = NXOpen.Point3d(199.99999999999997, 175.00000000000003, 25.0)
    point2_11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_11, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_11)
    
    point1_12 = NXOpen.Point3d(199.99999999999997, 175.00000000000003, 25.0)
    point2_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_12, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_12)
    
    point1_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_13, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_13)
    
    dimensionlinearunits217 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits218 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits219 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits220 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits221 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits222 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    edge3 = extrude1.FindObject("EDGE * 150 * 160 {(200,200,150)(200,200,75)(200,200,0) EXTRUDE(2)}")
    point21 = NXOpen.Point3d(199.99999999999997, 200.00000000000003, 34.914423351184247)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(edge3, workPart.ModelingViews.WorkView, point21)
    
    point1_14 = NXOpen.Point3d(199.99999999999997, 200.00000000000003, 34.914423351184247)
    point2_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge3, workPart.ModelingViews.WorkView, point1_14, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_14)
    
    point1_15 = NXOpen.Point3d(199.99999999999997, 175.00000000000003, 25.0)
    point2_15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_15, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_15)
    
    point1_16 = NXOpen.Point3d(199.99999999999997, 200.00000000000003, 34.914423351184247)
    point2_16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge3, workPart.ModelingViews.WorkView, point1_16, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_16)
    
    point1_17 = NXOpen.Point3d(199.99999999999997, 175.00000000000003, 25.0)
    point2_17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_17, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_17)
    
    dimensionlinearunits223 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits224 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits225 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits226 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits227 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits228 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits229 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits230 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits231 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits232 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits233 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits234 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin7 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin7.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin7.View = NXOpen.View.Null
    assocOrigin7.ViewOfGeometry = workPart.ModelingViews.WorkView
    point22 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin7.PointOnGeometry = point22
    assocOrigin7.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.DimensionLine = 0
    assocOrigin7.AssociatedView = NXOpen.View.Null
    assocOrigin7.AssociatedPoint = NXOpen.Point.Null
    assocOrigin7.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.XOffsetFactor = 0.0
    assocOrigin7.YOffsetFactor = 0.0
    assocOrigin7.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder9.Origin.SetAssociativeOrigin(assocOrigin7)
    
    point23 = NXOpen.Point3d(199.99999999999997, 186.68309059572869, 50.961757981495424)
    sketchRapidDimensionBuilder9.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point23)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.TextCentered = True
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject9 = sketchRapidDimensionBuilder9.Commit()
    
    theSession.DeleteUndoMark(markId51, None)
    
    theSession.SetUndoMarkName(markId50, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId50, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder9.Destroy()
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder10 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines49 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBefore(lines49)
    
    lines50 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAfter(lines50)
    
    lines51 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAbove(lines51)
    
    lines52 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBelow(lines52)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder10.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId52, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder10.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits235 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits236 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits237 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits238 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits239 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits240 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits241 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits242 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits243 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits244 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder10.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits245 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits246 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits247 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits248 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits249 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits250 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits251 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits252 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits253 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits254 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    expression20 = workPart.Expressions.FindObject("p13")
    expression20.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId52, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId53, None)
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId52, "Edit Driving Value")
    
    point1_18 = NXOpen.Point3d(199.99999999999997, 180.00000000000003, 25.0)
    point2_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_18, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_18)
    
    point1_19 = NXOpen.Point3d(199.99999999999997, 180.00000000000003, 25.0)
    point2_19 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_19, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_19)
    
    point1_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_20, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_20)
    
    dimensionlinearunits255 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits256 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits257 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits258 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits259 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits260 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    point24 = NXOpen.Point3d(199.99999999999997, 173.23164833208546, 0.0)
    sketchRapidDimensionBuilder10.SecondAssociativity.SetValue(line2, workPart.ModelingViews.WorkView, point24)
    
    point1_21 = NXOpen.Point3d(199.99999999999997, 173.23164833208546, 0.0)
    point2_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line2, workPart.ModelingViews.WorkView, point1_21, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_21)
    
    point1_22 = NXOpen.Point3d(199.99999999999997, 180.00000000000003, 25.0)
    point2_22 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_22, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_22)
    
    point1_23 = NXOpen.Point3d(199.99999999999997, 173.23164833208546, 0.0)
    point2_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line2, workPart.ModelingViews.WorkView, point1_23, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_23)
    
    point1_24 = NXOpen.Point3d(199.99999999999997, 180.00000000000003, 25.0)
    point2_24 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_24, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_24)
    
    dimensionlinearunits261 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits262 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits263 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits264 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits265 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits266 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits267 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits268 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits269 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits270 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits271 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits272 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin8 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin8.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin8.View = NXOpen.View.Null
    assocOrigin8.ViewOfGeometry = workPart.ModelingViews.WorkView
    point25 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin8.PointOnGeometry = point25
    assocOrigin8.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.DimensionLine = 0
    assocOrigin8.AssociatedView = NXOpen.View.Null
    assocOrigin8.AssociatedPoint = NXOpen.Point.Null
    assocOrigin8.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.XOffsetFactor = 0.0
    assocOrigin8.YOffsetFactor = 0.0
    assocOrigin8.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder10.Origin.SetAssociativeOrigin(assocOrigin8)
    
    point26 = NXOpen.Point3d(199.99999999999997, 148.21668552601216, 8.0115388238978227)
    sketchRapidDimensionBuilder10.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point26)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.TextCentered = False
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject10 = sketchRapidDimensionBuilder10.Commit()
    
    theSession.DeleteUndoMark(markId55, None)
    
    theSession.SetUndoMarkName(markId54, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId54, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder10.Destroy()
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder11 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines53 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBefore(lines53)
    
    lines54 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAfter(lines54)
    
    lines55 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAbove(lines55)
    
    lines56 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBelow(lines56)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder11.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId56, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder11.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits273 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits274 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits275 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits276 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits277 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits278 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits279 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits280 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits281 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits282 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder11.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits283 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits284 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits285 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits286 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits287 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits288 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits289 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits290 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits291 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits292 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    expression21 = workPart.Expressions.FindObject("p14")
    expression21.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId56, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId57, None)
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId56, "Edit Driving Value")
    
    point1_25 = NXOpen.Point3d(199.99999999999997, 180.00000000000003, 20.0)
    point2_25 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_25, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_25)
    
    point1_26 = NXOpen.Point3d(199.99999999999997, 180.00000000000003, 20.0)
    point2_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_26, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_26)
    
    point1_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_27, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_27)
    
    dimensionlinearunits293 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits294 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits295 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits296 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits297 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits298 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin9 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin9.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin9.View = NXOpen.View.Null
    assocOrigin9.ViewOfGeometry = workPart.ModelingViews.WorkView
    point27 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin9.PointOnGeometry = point27
    assocOrigin9.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin9.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin9.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.DimensionLine = 0
    assocOrigin9.AssociatedView = NXOpen.View.Null
    assocOrigin9.AssociatedPoint = NXOpen.Point.Null
    assocOrigin9.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin9.XOffsetFactor = 0.0
    assocOrigin9.YOffsetFactor = 0.0
    assocOrigin9.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder11.Origin.SetAssociativeOrigin(assocOrigin9)
    
    point28 = NXOpen.Point3d(199.99999999999997, 210.51810232604385, 26.890756036028634)
    sketchRapidDimensionBuilder11.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point28)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.TextCentered = False
    
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject11 = sketchRapidDimensionBuilder11.Commit()
    
    theSession.DeleteUndoMark(markId59, None)
    
    theSession.SetUndoMarkName(markId58, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId58, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder11.Destroy()
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder12 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines57 = []
    sketchRapidDimensionBuilder12.AppendedText.SetBefore(lines57)
    
    lines58 = []
    sketchRapidDimensionBuilder12.AppendedText.SetAfter(lines58)
    
    lines59 = []
    sketchRapidDimensionBuilder12.AppendedText.SetAbove(lines59)
    
    lines60 = []
    sketchRapidDimensionBuilder12.AppendedText.SetBelow(lines60)
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder12.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId60, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder12.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits299 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits300 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits301 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits302 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits303 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits304 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits305 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits306 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits307 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits308 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder12.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits309 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits310 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits311 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits312 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits313 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits314 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits315 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits316 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits317 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits318 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    expression22 = workPart.Expressions.FindObject("p15")
    expression22.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId60, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId61, None)
    
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId60, "Edit Driving Value")
    
    sketchRapidDimensionBuilder12.Destroy()
    
    theSession.UndoToMark(markId62, None)
    
    theSession.DeleteUndoMark(markId62, None)
    
    sketchRapidDimensionBuilder12.Destroy()
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = -0.7255212284411553
    rotMatrix3.Xy = 0.67723289611219839
    rotMatrix3.Xz = -0.12237054998945407
    rotMatrix3.Yx = -0.29640022284305473
    rotMatrix3.Yy = -0.14701882593764662
    rotMatrix3.Yz = 0.94368022800019713
    rotMatrix3.Zx = 0.62110051922359966
    rotMatrix3.Zy = 0.72093069656063358
    rotMatrix3.Zz = 0.30739726052256067
    translation3 = NXOpen.Point3d(40.525345848561649, 7.8923080380367452, -265.97446851679172)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 1.1211623039680929)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder2.Section = section2
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder2.DistanceTolerance = 0.01
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("150")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies3 = [NXOpen.Body.Null] * 1 
    targetBodies3[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies3)
    
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId63, "拉伸 對話方塊")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 2 
    curves1[0] = arc2
    curves1[1] = arc1
    seedPoint1 = NXOpen.Point3d(199.99999999999997, 19.999999999999989, 16.666666666666664)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(theSession.ActiveSketch, curves1, seedPoint1, 0.01)
    
    curves2 = [NXOpen.ICurve.Null] * 2 
    curves2[0] = arc2
    curves2[1] = arc1
    seedPoint2 = NXOpen.Point3d(199.99999999999997, 183.33333333333334, 19.999999999999989)
    regionBoundaryRule2 = workPart.ScRuleFactory.CreateRuleRegionBoundary(theSession.ActiveSketch, curves2, seedPoint2, 0.01)
    
    section2.AllowSelfIntersection(True)
    
    rules2 = [None] * 2 
    rules2[0] = regionBoundaryRule1
    rules2[1] = regionBoundaryRule2
    helpPoint2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section2.AddToSection(rules2, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId64, None)
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId66, None)
    
    direction3 = workPart.Directions.CreateDirection(theSession.ActiveSketch, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder2.Direction = direction3
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    targetBodies4[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies4)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies5 = [NXOpen.Body.Null] * 1 
    targetBodies5[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies5)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId65, None)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies6)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies7 = [NXOpen.Body.Null] * 1 
    targetBodies7[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies7)
    
    extrudeBuilder2.Limits.StartExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.UntilNext
    
    extrudeBuilder2.Limits.StartExtend.Target = NXOpen.DisplayableObject.Null
    
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId67, None)
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder2.ParentFeatureInternal = False
    
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    feature4 = extrudeBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId68, None)
    
    theSession.SetUndoMarkName(markId63, "拉伸")
    
    expression26 = extrudeBuilder2.Limits.EndExtend.Value
    extrudeBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression23)
    
    workPart.Expressions.Delete(expression24)
    
    workPart.Expressions.Delete(expression25)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = -0.76751108067107054
    rotMatrix4.Xy = 0.62979079812669447
    rotMatrix4.Xz = 0.11954200785526702
    rotMatrix4.Yx = -0.065808985684025101
    rotMatrix4.Yy = -0.26290816040754639
    rotMatrix4.Yz = 0.96257388110958098
    rotMatrix4.Zx = 0.6376487422165652
    rotMatrix4.Zy = 0.73091918143257406
    rotMatrix4.Zz = 0.24323081992948947
    translation4 = NXOpen.Point3d(31.325099031749527, -4.9949062140800322, -263.81565625880188)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 1.1211623039680929)
    
    scaleAboutPoint24 = NXOpen.Point3d(57.581612496998943, -53.097798409117971, 0.0)
    viewCenter24 = NXOpen.Point3d(-57.581612496999085, 53.097798409117893, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(71.977015621248626, -66.37224801139746, 0.0)
    viewCenter25 = NXOpen.Point3d(-71.977015621248825, 66.372248011397389, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(167.03682416201676, -99.189637305921707, 0.0)
    viewCenter26 = NXOpen.Point3d(-167.03682416201687, 99.18963730592165, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(209.71786698045696, -125.36980179930625, 0.0)
    viewCenter27 = NXOpen.Point3d(-209.71786698045713, 125.36980179930616, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(262.14733372557117, -156.71225224913286, 0.0)
    viewCenter28 = NXOpen.Point3d(-262.1473337255714, 156.71225224913269, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint28, viewCenter28)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = -0.28321415630907215
    rotMatrix5.Xy = -0.94882240013273578
    rotMatrix5.Xz = -0.13973472965766759
    rotMatrix5.Yx = 0.25363071764167089
    rotMatrix5.Yy = -0.21461196332371205
    rotMatrix5.Yz = 0.9431930683942269
    rotMatrix5.Zx = -0.92491145561870725
    rotMatrix5.Zy = 0.23168460933929647
    rotMatrix5.Zz = 0.30143165238671549
    translation5 = NXOpen.Point3d(352.3176449815362, -165.5003697451005, -62.001241700238836)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.3673824637642647)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = -0.39997588266195622
    rotMatrix6.Xy = -0.91099378563423195
    rotMatrix6.Xz = 0.10054658534534822
    rotMatrix6.Yx = 0.4888764637307636
    rotMatrix6.Yy = -0.1192656692260448
    rotMatrix6.Yz = 0.86416173448850064
    rotMatrix6.Zx = -0.77525421411231299
    rotMatrix6.Zy = 0.39479871159856145
    rotMatrix6.Zz = 0.49306681172151828
    translation6 = NXOpen.Point3d(342.1898575417481, -192.63222372084704, -107.65101302691491)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.3673824637642647)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = -0.81151863900583021
    rotMatrix7.Xy = -0.4319293132823
    rotMatrix7.Xz = 0.3935410612294552
    rotMatrix7.Yx = 0.55337415160993508
    rotMatrix7.Yy = -0.3518004890627075
    rotMatrix7.Yz = 0.75499236037540451
    rotMatrix7.Zx = -0.18765539394355199
    rotMatrix7.Zy = 0.83046582363317079
    rotMatrix7.Zz = 0.52451117137880843
    translation7 = NXOpen.Point3d(313.46310024963435, -167.64080746661577, -212.33593322154871)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 0.3673824637642647)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = -0.80477358586910352
    rotMatrix8.Xy = -0.51969072553975337
    rotMatrix8.Xz = 0.28681182903665037
    rotMatrix8.Yx = -0.40314003560221667
    rotMatrix8.Yy = 0.83318783728332468
    rotMatrix8.Yz = 0.37851834763691578
    rotMatrix8.Zx = -0.43568060225585864
    rotMatrix8.Zy = 0.18899623697603676
    rotMatrix8.Zz = -0.88003570110926288
    translation8 = NXOpen.Point3d(329.5694285761673, -162.25267042461724, -18.045438287999282)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 0.3673824637642647)
    
    scaleAboutPoint29 = NXOpen.Point3d(94.344232741895112, -60.495538552054995, 0.0)
    viewCenter29 = NXOpen.Point3d(-94.34423274189524, 60.495538552054875, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint29, viewCenter29)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder3 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.PlaneReference = plane5
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder3 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder3.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId70, "建立草圖 對話方塊")
    
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = 0.01027211718412935
    rotMatrix9.Xy = -0.96626478344830269
    rotMatrix9.Xz = 0.25734578270522135
    rotMatrix9.Yx = 0.77961508229418963
    rotMatrix9.Yy = 0.16889938648538902
    rotMatrix9.Yz = 0.60305333155889729
    rotMatrix9.Zx = -0.62617474164004749
    rotMatrix9.Zy = 0.19443601907174143
    rotMatrix9.Zz = 0.75504955295633047
    translation9 = NXOpen.Point3d(318.51827572203007, -246.06334556662657, -122.17139661407035)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 0.29390597101141175)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = -0.89400387621971422
    rotMatrix10.Xy = -0.21138613837850609
    rotMatrix10.Xz = 0.39506071660638392
    rotMatrix10.Yx = 0.088998109480027413
    rotMatrix10.Yy = 0.78036957639249782
    rotMatrix10.Yz = 0.61895287441773594
    rotMatrix10.Zx = -0.43913142202888206
    rotMatrix10.Zy = 0.58850592583458294
    rotMatrix10.Zz = -0.67884045949285932
    translation10 = NXOpen.Point3d(323.12939051284752, -239.34113299033413, -72.740968317781807)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 0.29390597101141175)
    
    scalar3 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge4 = extrude1.FindObject("EDGE * 120 * 170 {(0,200,0)(0,100,0)(0,0,0) EXTRUDE(2)}")
    point29 = workPart.Points.CreatePoint(edge4, scalar3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge5 = extrude1.FindObject("EDGE * 120 * 160 {(200,200,0)(100,200,0)(0,200,0) EXTRUDE(2)}")
    direction4 = workPart.Directions.CreateDirection(edge5, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face2 = extrude1.FindObject("FACE 120 {(100,100,0) EXTRUDE(2)}")
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(face2, direction4, point29, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.Csystem = cartesianCoordinateSystem2
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane6 = workPart.Planes.CreatePlane(origin6, normal6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane6.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom4 = [NXOpen.NXObject.Null] * 1 
    geom4[0] = face2
    plane6.SetGeometry(geom4)
    
    plane6.SetFlip(False)
    
    plane6.SetExpression(None)
    
    plane6.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane6.Evaluate()
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane7.SynchronizeToPlane(plane6)
    
    scalar4 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point30 = workPart.Points.CreatePoint(edge4, scalar4, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane7.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom5 = [NXOpen.NXObject.Null] * 1 
    geom5[0] = face2
    plane7.SetGeometry(geom5)
    
    plane7.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane7.Evaluate()
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId71, None)
    
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject12 = sketchInPlaceBuilder3.Commit()
    
    sketch4 = nXObject12
    feature5 = sketch4.Feature
    
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs5 = theSession.UpdateManager.DoUpdate(markId73)
    
    sketch4.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId72, None)
    
    theSession.SetUndoMarkName(markId70, "建立草圖")
    
    sketchInPlaceBuilder3.Destroy()
    
    sketchAlongPathBuilder3.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression28)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point30)
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression27)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane5.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression30)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression29)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane7.DestroyPlane()
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->矩形(R)...
    # ----------------------------------------------
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId75, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint5 = NXOpen.Point3d(117.93029092736904, 200.00000000000003, 0.0)
    endPoint5 = NXOpen.Point3d(67.930290927369043, 200.00000000000003, 0.0)
    line5 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    
    startPoint6 = NXOpen.Point3d(67.930290927369043, 200.00000000000003, 0.0)
    endPoint6 = NXOpen.Point3d(67.930290927369029, 285.0, 0.0)
    line6 = workPart.Curves.CreateLine(startPoint6, endPoint6)
    
    startPoint7 = NXOpen.Point3d(67.930290927369029, 285.0, 0.0)
    endPoint7 = NXOpen.Point3d(117.93029092736903, 285.0, 0.0)
    line7 = workPart.Curves.CreateLine(startPoint7, endPoint7)
    
    startPoint8 = NXOpen.Point3d(117.93029092736903, 285.0, 0.0)
    endPoint8 = NXOpen.Point3d(117.93029092736904, 200.00000000000003, 0.0)
    line8 = workPart.Curves.CreateLine(startPoint8, endPoint8)
    
    theSession.ActiveSketch.AddGeometry(line5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line7, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line8, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_6.Geometry = line5
    geom1_6.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_6.SplineDefiningPointIndex = 0
    geom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_6.Geometry = line6
    geom2_6.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint11 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_6, geom2_6)
    
    geom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_7.Geometry = line6
    geom1_7.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_7.SplineDefiningPointIndex = 0
    geom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_7.Geometry = line7
    geom2_7.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint12 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_7, geom2_7)
    
    geom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_8.Geometry = line7
    geom1_8.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_8.SplineDefiningPointIndex = 0
    geom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_8.Geometry = line8
    geom2_8.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint13 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_8, geom2_8)
    
    geom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_9.Geometry = line8
    geom1_9.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_9.SplineDefiningPointIndex = 0
    geom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_9.Geometry = line5
    geom2_9.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint14 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_9, geom2_9)
    
    geom6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom6.Geometry = line5
    geom6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint15 = theSession.ActiveSketch.CreateHorizontalConstraint(geom6)
    
    conGeom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_5.Geometry = line5
    conGeom1_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_5.SplineDefiningPointIndex = 0
    conGeom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_5.Geometry = line6
    conGeom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint16 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_5, conGeom2_5)
    
    conGeom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_6.Geometry = line6
    conGeom1_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_6.SplineDefiningPointIndex = 0
    conGeom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_6.Geometry = line7
    conGeom2_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint17 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_6, conGeom2_6)
    
    conGeom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_7.Geometry = line7
    conGeom1_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_7.SplineDefiningPointIndex = 0
    conGeom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_7.Geometry = line8
    conGeom2_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint18 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_7, conGeom2_7)
    
    conGeom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_8.Geometry = line8
    conGeom1_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_8.SplineDefiningPointIndex = 0
    conGeom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_8.Geometry = line5
    conGeom2_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint19 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_8, conGeom2_8)
    
    conGeom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_9.Geometry = line5
    conGeom1_9.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_9.SplineDefiningPointIndex = 0
    conGeom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_9.Geometry = line3
    conGeom2_9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_9.SplineDefiningPointIndex = 0
    help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help1.Point.X = 117.93029092736904
    help1.Point.Y = 200.00000000000003
    help1.Point.Z = 0.0
    help1.Parameter = 0.0
    sketchHelpedGeometricConstraint1 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_9, conGeom2_9, help1)
    
    dimObject1_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_5.Geometry = line5
    dimObject1_5.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_5.AssocValue = 0
    dimObject1_5.HelpPoint.X = 0.0
    dimObject1_5.HelpPoint.Y = 0.0
    dimObject1_5.HelpPoint.Z = 0.0
    dimObject1_5.View = NXOpen.NXObject.Null
    dimObject2_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_3.Geometry = line5
    dimObject2_3.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_3.AssocValue = 0
    dimObject2_3.HelpPoint.X = 0.0
    dimObject2_3.HelpPoint.Y = 0.0
    dimObject2_3.HelpPoint.Z = 0.0
    dimObject2_3.View = NXOpen.NXObject.Null
    dimOrigin5 = NXOpen.Point3d(92.930290927369043, 169.37796136285186, 0.0)
    sketchDimensionalConstraint5 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_5, dimObject2_3, dimOrigin5, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint3 = sketchDimensionalConstraint5
    dimension5 = sketchHelpedDimensionalConstraint3.AssociatedDimension
    
    expression31 = sketchHelpedDimensionalConstraint3.AssociatedExpression
    
    dimObject1_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_6.Geometry = line6
    dimObject1_6.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_6.AssocValue = 0
    dimObject1_6.HelpPoint.X = 0.0
    dimObject1_6.HelpPoint.Y = 0.0
    dimObject1_6.HelpPoint.Z = 0.0
    dimObject1_6.View = NXOpen.NXObject.Null
    dimObject2_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_4.Geometry = line6
    dimObject2_4.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_4.AssocValue = 0
    dimObject2_4.HelpPoint.X = 0.0
    dimObject2_4.HelpPoint.Y = 0.0
    dimObject2_4.HelpPoint.Z = 0.0
    dimObject2_4.View = NXOpen.NXObject.Null
    dimOrigin6 = NXOpen.Point3d(37.308252290220871, 242.5, 0.0)
    sketchDimensionalConstraint6 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_6, dimObject2_4, dimOrigin6, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint4 = sketchDimensionalConstraint6
    dimension6 = sketchHelpedDimensionalConstraint4.AssociatedDimension
    
    expression32 = sketchHelpedDimensionalConstraint4.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms3 = [NXOpen.SmartObject.Null] * 4 
    geoms3[0] = line5
    geoms3[1] = line6
    geoms3[2] = line7
    geoms3[3] = line8
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms3)
    
    geoms4 = [NXOpen.SmartObject.Null] * 4 
    geoms4[0] = line5
    geoms4[1] = line6
    geoms4[2] = line7
    geoms4[3] = line8
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms4)
    
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.DeleteUndoMark(markId76, "Create Rectangle")
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete3 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId78 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "起點")
    
    theSession.SetUndoMarkName(markId78, "類選取 對話方塊")
    
    markId79 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "類選取")
    
    theSession.DeleteUndoMark(markId79, None)
    
    markId80 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "類選取")
    
    theSession.DeleteUndoMark(markId80, None)
    
    theSession.SetUndoMarkName(markId78, "類選取")
    
    theSession.DeleteUndoMark(markId78, None)
    
    markId81 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects2 = [NXOpen.TaggedObject.Null] * 5 
    objects2[0] = line7
    sketchHelpedGeometricConstraint2 = sketchGeometricConstraint12
    objects2[1] = sketchHelpedGeometricConstraint2
    sketchHelpedGeometricConstraint3 = sketchGeometricConstraint13
    objects2[2] = sketchHelpedGeometricConstraint3
    objects2[3] = sketchGeometricConstraint17
    objects2[4] = sketchGeometricConstraint18
    nErrs6 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    notifyOnDelete4 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id2 = theSession.NewestVisibleUndoMark
    
    nErrs7 = theSession.UpdateManager.DoUpdate(id2)
    
    theSession.DeleteUndoMark(markId77, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId82 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete5 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId83 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = line6
    nErrs8 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    notifyOnDelete6 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id3 = theSession.NewestVisibleUndoMark
    
    nErrs9 = theSession.UpdateManager.DoUpdate(id3)
    
    theSession.DeleteUndoMark(markId82, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId84 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete7 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId85 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    objects4[0] = line8
    nErrs10 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    notifyOnDelete8 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id4 = theSession.NewestVisibleUndoMark
    
    nErrs11 = theSession.UpdateManager.DoUpdate(id4)
    
    theSession.DeleteUndoMark(markId84, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId86 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete9 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId87 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "起點")
    
    theSession.SetUndoMarkName(markId87, "類選取 對話方塊")
    
    theSession.SetUndoMarkName(markId87, "類選取")
    
    theSession.DeleteUndoMark(markId87, None)
    
    theSession.DeleteUndoMark(markId86, None)
    
    scaleAboutPoint30 = NXOpen.Point3d(-151.23884638013735, -19.805087025970394, 0.0)
    viewCenter30 = NXOpen.Point3d(151.23884638013735, 19.805087025970316, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(-117.3901521902971, -16.564254603538831, 0.0)
    viewCenter31 = NXOpen.Point3d(117.3901521902971, 16.564254603538831, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(-93.335973766027564, -13.251403682831064, 0.0)
    viewCenter32 = NXOpen.Point3d(93.335973766027621, 13.251403682831064, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(-69.598676734173608, -11.062041335232863, 0.0)
    viewCenter33 = NXOpen.Point3d(69.59867673417385, 11.062041335232902, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(-25.811429782210016, -7.0059595123141483, 0.0)
    viewCenter34 = NXOpen.Point3d(25.811429782210205, 7.0059595123141483, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId88 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete10 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId89 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects5 = [NXOpen.TaggedObject.Null] * 1 
    objects5[0] = line5
    nErrs12 = theSession.UpdateManager.AddObjectsToDeleteList(objects5)
    
    notifyOnDelete11 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id5 = theSession.NewestVisibleUndoMark
    
    nErrs13 = theSession.UpdateManager.DoUpdate(id5)
    
    theSession.DeleteUndoMark(markId88, None)
    
    scaleAboutPoint35 = NXOpen.Point3d(2.0649143825768919, 5.3097798409118173, 0.0)
    viewCenter35 = NXOpen.Point3d(-2.0649143825766907, -5.3097798409117667, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(2.5811429782210826, 7.0059595123141785, 0.0)
    viewCenter36 = NXOpen.Point3d(-2.5811429782207682, -7.0059595123141785, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(3.2264287227763928, 8.7574493903927628, 0.0)
    viewCenter37 = NXOpen.Point3d(-3.2264287227760784, -8.7574493903926847, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint37, viewCenter37)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId90 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId91 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId91, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint9 = NXOpen.Point3d(153.93867584351753, 200.00000000000003, 0.0)
    endPoint9 = NXOpen.Point3d(199.99999999999994, 325.23095013462978, 0.0)
    line9 = workPart.Curves.CreateLine(startPoint9, endPoint9)
    
    theSession.ActiveSketch.AddGeometry(line9, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_10.Geometry = line9
    conGeom1_10.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_10.SplineDefiningPointIndex = 0
    conGeom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_10.Geometry = line3
    conGeom2_10.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_10.SplineDefiningPointIndex = 0
    help2 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help2.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help2.Point.X = 153.93867584351753
    help2.Point.Y = 200.00000000000003
    help2.Point.Z = 0.0
    help2.Parameter = 0.0
    sketchHelpedGeometricConstraint4 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_10, conGeom2_10, help2)
    
    dimObject1_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_7.Geometry = line9
    dimObject1_7.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_7.AssocValue = 0
    dimObject1_7.HelpPoint.X = 0.0
    dimObject1_7.HelpPoint.Y = 0.0
    dimObject1_7.HelpPoint.Z = 0.0
    dimObject1_7.View = NXOpen.NXObject.Null
    dimObject2_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_5.Geometry = line9
    dimObject2_5.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_5.AssocValue = 0
    dimObject2_5.HelpPoint.X = 0.0
    dimObject2_5.HelpPoint.Y = 0.0
    dimObject2_5.HelpPoint.Z = 0.0
    dimObject2_5.View = NXOpen.NXObject.Null
    dimOrigin7 = NXOpen.Point3d(158.57595409101441, 269.38076443110003, 0.0)
    sketchDimensionalConstraint7 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_7, dimObject2_5, dimOrigin7, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint5 = sketchDimensionalConstraint7
    dimension7 = sketchHelpedDimensionalConstraint5.AssociatedDimension
    
    expression33 = sketchHelpedDimensionalConstraint5.AssociatedExpression
    
    dimObject1_8 = NXOpen.Sketch.DimensionGeometry()
    
    datumAxis2 = workPart.Datums.FindObject("SKETCH(5:1B) X axis")
    dimObject1_8.Geometry = datumAxis2
    dimObject1_8.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject1_8.AssocValue = 0
    dimObject1_8.HelpPoint.X = -28.574999999999999
    dimObject1_8.HelpPoint.Y = 200.0
    dimObject1_8.HelpPoint.Z = 0.0
    dimObject1_8.View = NXOpen.NXObject.Null
    dimObject2_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_6.Geometry = line9
    dimObject2_6.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_6.AssocValue = 0
    dimObject2_6.HelpPoint.X = 199.99999999999994
    dimObject2_6.HelpPoint.Y = 325.23095013462978
    dimObject2_6.HelpPoint.Z = 0.0
    dimObject2_6.View = NXOpen.NXObject.Null
    dimOrigin8 = NXOpen.Point3d(142.72487052472255, 216.07284290948544, 0.0)
    sketchDimensionalConstraint8 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_8, dimObject2_6, dimOrigin8, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension8 = sketchDimensionalConstraint8.AssociatedDimension
    
    expression34 = sketchDimensionalConstraint8.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId92 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId92, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint10 = NXOpen.Point3d(153.9386758435175, 325.23095013462978, 0.0)
    endPoint10 = NXOpen.Point3d(107.27068896050403, 199.99999999999994, 0.0)
    line10 = workPart.Curves.CreateLine(startPoint10, endPoint10)
    
    theSession.ActiveSketch.AddGeometry(line10, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_11 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_11.Geometry = line10
    conGeom1_11.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_11.SplineDefiningPointIndex = 0
    conGeom2_11 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_11.Geometry = line3
    conGeom2_11.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_11.SplineDefiningPointIndex = 0
    help3 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help3.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help3.Point.X = 107.27068896050375
    help3.Point.Y = 200.00000000000003
    help3.Point.Z = 0.0
    help3.Parameter = 0.0
    sketchHelpedGeometricConstraint5 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_11, conGeom2_11, help3)
    
    dimObject1_9 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_9.Geometry = line10
    dimObject1_9.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_9.AssocValue = 0
    dimObject1_9.HelpPoint.X = 0.0
    dimObject1_9.HelpPoint.Y = 0.0
    dimObject1_9.HelpPoint.Z = 0.0
    dimObject1_9.View = NXOpen.NXObject.Null
    dimObject2_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_7.Geometry = line10
    dimObject2_7.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_7.AssocValue = 0
    dimObject2_7.HelpPoint.X = 0.0
    dimObject2_7.HelpPoint.Y = 0.0
    dimObject2_7.HelpPoint.Z = 0.0
    dimObject2_7.View = NXOpen.NXObject.Null
    dimOrigin9 = NXOpen.Point3d(148.96907677566116, 255.77188476617403, 0.0)
    sketchDimensionalConstraint9 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_9, dimObject2_7, dimOrigin9, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint6 = sketchDimensionalConstraint9
    dimension9 = sketchHelpedDimensionalConstraint6.AssociatedDimension
    
    expression35 = sketchHelpedDimensionalConstraint6.AssociatedExpression
    
    dimObject1_10 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_10.Geometry = datumAxis2
    dimObject1_10.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject1_10.AssocValue = 0
    dimObject1_10.HelpPoint.X = -28.574999999999999
    dimObject1_10.HelpPoint.Y = 200.0
    dimObject1_10.HelpPoint.Z = 0.0
    dimObject1_10.View = NXOpen.NXObject.Null
    dimObject2_8 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_8.Geometry = line10
    dimObject2_8.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject2_8.AssocValue = 0
    dimObject2_8.HelpPoint.X = 153.9386758435175
    dimObject2_8.HelpPoint.Y = 325.23095013462978
    dimObject2_8.HelpPoint.Z = 0.0
    dimObject2_8.View = NXOpen.NXObject.Null
    dimOrigin10 = NXOpen.Point3d(96.091147165665362, 216.096693889687, 0.0)
    sketchDimensionalConstraint10 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_10, dimObject2_8, dimOrigin10, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension10 = sketchDimensionalConstraint10.AssociatedDimension
    
    expression36 = sketchDimensionalConstraint10.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId93 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId93, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint11 = NXOpen.Point3d(69.821069856850755, 200.0, 0.0)
    endPoint11 = NXOpen.Point3d(18.543899084156575, 325.23095013462978, 0.0)
    line11 = workPart.Curves.CreateLine(startPoint11, endPoint11)
    
    theSession.ActiveSketch.AddGeometry(line11, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_12 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_12.Geometry = line11
    conGeom1_12.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_12.SplineDefiningPointIndex = 0
    conGeom2_12 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_12.Geometry = line3
    conGeom2_12.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_12.SplineDefiningPointIndex = 0
    help4 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help4.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help4.Point.X = 69.821069856850755
    help4.Point.Y = 200.0
    help4.Point.Z = 0.0
    help4.Parameter = 0.0
    sketchHelpedGeometricConstraint6 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_12, conGeom2_12, help4)
    
    dimObject1_11 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_11.Geometry = line11
    dimObject1_11.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_11.AssocValue = 0
    dimObject1_11.HelpPoint.X = 0.0
    dimObject1_11.HelpPoint.Y = 0.0
    dimObject1_11.HelpPoint.Z = 0.0
    dimObject1_11.View = NXOpen.NXObject.Null
    dimObject2_9 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_9.Geometry = line11
    dimObject2_9.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_9.AssocValue = 0
    dimObject2_9.HelpPoint.X = 0.0
    dimObject2_9.HelpPoint.Y = 0.0
    dimObject2_9.HelpPoint.Z = 0.0
    dimObject2_9.View = NXOpen.NXObject.Null
    dimOrigin11 = NXOpen.Point3d(26.04587046192815, 255.18924175393371, 0.0)
    sketchDimensionalConstraint11 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_11, dimObject2_9, dimOrigin11, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint7 = sketchDimensionalConstraint11
    dimension11 = sketchHelpedDimensionalConstraint7.AssociatedDimension
    
    expression37 = sketchHelpedDimensionalConstraint7.AssociatedExpression
    
    dimObject1_12 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_12.Geometry = datumAxis2
    dimObject1_12.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject1_12.AssocValue = 0
    dimObject1_12.HelpPoint.X = -28.574999999999999
    dimObject1_12.HelpPoint.Y = 200.0
    dimObject1_12.HelpPoint.Z = 0.0
    dimObject1_12.View = NXOpen.NXObject.Null
    dimObject2_10 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_10.Geometry = line11
    dimObject2_10.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_10.AssocValue = 0
    dimObject2_10.HelpPoint.X = 18.543899084156575
    dimObject2_10.HelpPoint.Y = 325.23095013462978
    dimObject2_10.HelpPoint.Z = 0.0
    dimObject2_10.View = NXOpen.NXObject.Null
    dimOrigin12 = NXOpen.Point3d(53.547996896752458, 210.92120896953026, 0.0)
    sketchDimensionalConstraint12 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_12, dimObject2_10, dimOrigin12, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension12 = sketchDimensionalConstraint12.AssociatedDimension
    
    expression38 = sketchDimensionalConstraint12.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId94 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId94, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint12 = NXOpen.Point3d(35.25219068424795, 200.0, 0.0)
    endPoint12 = NXOpen.Point3d(-10.399657444197837, 311.49258491405453, 0.0)
    line12 = workPart.Curves.CreateLine(startPoint12, endPoint12)
    
    theSession.ActiveSketch.AddGeometry(line12, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_13 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_13.Geometry = line12
    conGeom1_13.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_13.SplineDefiningPointIndex = 0
    conGeom2_13 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_13.Geometry = line3
    conGeom2_13.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_13.SplineDefiningPointIndex = 0
    help5 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help5.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help5.Point.X = 35.25219068424795
    help5.Point.Y = 200.0
    help5.Point.Z = 0.0
    help5.Parameter = 0.0
    sketchHelpedGeometricConstraint7 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_13, conGeom2_13, help5)
    
    conGeom1_14 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_14.Geometry = line12
    conGeom1_14.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_14.SplineDefiningPointIndex = 0
    conGeom2_14 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_14.Geometry = line11
    conGeom2_14.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_14.SplineDefiningPointIndex = 0
    sketchGeometricConstraint20 = theSession.ActiveSketch.CreateParallelConstraint(conGeom1_14, conGeom2_14)
    
    dimObject1_13 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_13.Geometry = line12
    dimObject1_13.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_13.AssocValue = 0
    dimObject1_13.HelpPoint.X = 0.0
    dimObject1_13.HelpPoint.Y = 0.0
    dimObject1_13.HelpPoint.Z = 0.0
    dimObject1_13.View = NXOpen.NXObject.Null
    dimObject2_11 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_11.Geometry = line12
    dimObject2_11.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_11.AssocValue = 0
    dimObject2_11.HelpPoint.X = 0.0
    dimObject2_11.HelpPoint.Y = 0.0
    dimObject2_11.HelpPoint.Z = 0.0
    dimObject2_11.View = NXOpen.NXObject.Null
    dimOrigin13 = NXOpen.Point3d(-5.7103473885504599, 248.32005914364609, 0.0)
    sketchDimensionalConstraint13 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_13, dimObject2_11, dimOrigin13, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint8 = sketchDimensionalConstraint13
    dimension13 = sketchHelpedDimensionalConstraint8.AssociatedDimension
    
    expression39 = sketchHelpedDimensionalConstraint8.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId95 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete12 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId96 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects6 = [NXOpen.TaggedObject.Null] * 1 
    objects6[0] = line10
    nErrs14 = theSession.UpdateManager.AddObjectsToDeleteList(objects6)
    
    notifyOnDelete13 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id6 = theSession.NewestVisibleUndoMark
    
    nErrs15 = theSession.UpdateManager.DoUpdate(id6)
    
    theSession.DeleteUndoMark(markId95, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId97 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete14 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId98 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "起點")
    
    theSession.SetUndoMarkName(markId98, "類選取 對話方塊")
    
    theSession.SetUndoMarkName(markId98, "類選取")
    
    theSession.DeleteUndoMark(markId98, None)
    
    theSession.DeleteUndoMark(markId97, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId99 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete15 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId100 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects7 = [NXOpen.TaggedObject.Null] * 1 
    objects7[0] = line9
    nErrs16 = theSession.UpdateManager.AddObjectsToDeleteList(objects7)
    
    notifyOnDelete16 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id7 = theSession.NewestVisibleUndoMark
    
    nErrs17 = theSession.UpdateManager.DoUpdate(id7)
    
    theSession.DeleteUndoMark(markId99, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId101 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete17 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId102 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects8 = [NXOpen.TaggedObject.Null] * 1 
    objects8[0] = line11
    nErrs18 = theSession.UpdateManager.AddObjectsToDeleteList(objects8)
    
    notifyOnDelete18 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id8 = theSession.NewestVisibleUndoMark
    
    nErrs19 = theSession.UpdateManager.DoUpdate(id8)
    
    theSession.DeleteUndoMark(markId101, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId103 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete19 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId104 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects9 = [NXOpen.TaggedObject.Null] * 1 
    objects9[0] = line12
    nErrs20 = theSession.UpdateManager.AddObjectsToDeleteList(objects9)
    
    notifyOnDelete20 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id9 = theSession.NewestVisibleUndoMark
    
    nErrs21 = theSession.UpdateManager.DoUpdate(id9)
    
    theSession.DeleteUndoMark(markId103, None)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId105 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId106 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId106, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint13 = NXOpen.Point3d(178.13689126433948, 200.00000000000003, 0.0)
    endPoint13 = NXOpen.Point3d(178.13689126433931, 325.0, 0.0)
    line13 = workPart.Curves.CreateLine(startPoint13, endPoint13)
    
    theSession.ActiveSketch.AddGeometry(line13, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_15 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_15.Geometry = line13
    conGeom1_15.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_15.SplineDefiningPointIndex = 0
    conGeom2_15 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_15.Geometry = line3
    conGeom2_15.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_15.SplineDefiningPointIndex = 0
    help6 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help6.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help6.Point.X = 178.13689126433948
    help6.Point.Y = 200.00000000000003
    help6.Point.Z = 0.0
    help6.Parameter = 0.0
    sketchHelpedGeometricConstraint8 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_15, conGeom2_15, help6)
    
    geom7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom7.Geometry = line13
    geom7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint21 = theSession.ActiveSketch.CreateVerticalConstraint(geom7)
    
    dimObject1_14 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_14.Geometry = line13
    dimObject1_14.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_14.AssocValue = 0
    dimObject1_14.HelpPoint.X = 0.0
    dimObject1_14.HelpPoint.Y = 0.0
    dimObject1_14.HelpPoint.Z = 0.0
    dimObject1_14.View = NXOpen.NXObject.Null
    dimObject2_12 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_12.Geometry = line13
    dimObject2_12.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_12.AssocValue = 0
    dimObject2_12.HelpPoint.X = 0.0
    dimObject2_12.HelpPoint.Y = 0.0
    dimObject2_12.HelpPoint.Z = 0.0
    dimObject2_12.View = NXOpen.NXObject.Null
    dimOrigin14 = NXOpen.Point3d(158.53878653656457, 262.5, 0.0)
    sketchDimensionalConstraint14 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_14, dimObject2_12, dimOrigin14, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint9 = sketchDimensionalConstraint14
    dimension14 = sketchHelpedDimensionalConstraint9.AssociatedDimension
    
    expression40 = sketchHelpedDimensionalConstraint9.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId107 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    markId108 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId108, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint14 = NXOpen.Point3d(178.13689126433934, 313.1318424242188, 0.0)
    endPoint14 = NXOpen.Point3d(178.13689126433934, 307.37036256211832, 0.0)
    line14 = workPart.Curves.CreateLine(startPoint14, endPoint14)
    
    theSession.ActiveSketch.AddGeometry(line14, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_16 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_16.Geometry = line14
    conGeom1_16.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_16.SplineDefiningPointIndex = 0
    conGeom2_16 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_16.Geometry = line13
    conGeom2_16.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_16.SplineDefiningPointIndex = 0
    help7 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help7.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help7.Point.X = 178.13689126433934
    help7.Point.Y = 313.1318424242188
    help7.Point.Z = 0.0
    help7.Parameter = 0.0
    sketchHelpedGeometricConstraint9 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_16, conGeom2_16, help7)
    
    geom8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom8.Geometry = line14
    geom8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint22 = theSession.ActiveSketch.CreateVerticalConstraint(geom8)
    
    conGeom1_17 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_17.Geometry = line14
    conGeom1_17.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_17.SplineDefiningPointIndex = 0
    conGeom2_17 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_17.Geometry = line13
    conGeom2_17.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_17.SplineDefiningPointIndex = 0
    help8 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help8.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help8.Point.X = 178.13689126433934
    help8.Point.Y = 307.37036256211832
    help8.Point.Z = 0.0
    help8.Parameter = 0.0
    sketchHelpedGeometricConstraint10 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_17, conGeom2_17, help8)
    
    dimObject1_15 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_15.Geometry = line14
    dimObject1_15.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_15.AssocValue = 0
    dimObject1_15.HelpPoint.X = 0.0
    dimObject1_15.HelpPoint.Y = 0.0
    dimObject1_15.HelpPoint.Z = 0.0
    dimObject1_15.View = NXOpen.NXObject.Null
    dimObject2_13 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_13.Geometry = line14
    dimObject2_13.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_13.AssocValue = 0
    dimObject2_13.HelpPoint.X = 0.0
    dimObject2_13.HelpPoint.Y = 0.0
    dimObject2_13.HelpPoint.Z = 0.0
    dimObject2_13.View = NXOpen.NXObject.Null
    dimOrigin15 = NXOpen.Point3d(197.73499599211416, 310.25110249316856, 0.0)
    sketchDimensionalConstraint15 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_15, dimObject2_13, dimOrigin15, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint10 = sketchDimensionalConstraint15
    dimension15 = sketchHelpedDimensionalConstraint10.AssociatedDimension
    
    expression41 = sketchHelpedDimensionalConstraint10.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId109 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId109, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint15 = NXOpen.Point3d(178.13689126433937, 288.93362700339679, 0.0)
    endPoint15 = NXOpen.Point3d(178.13689126433934, 306.2180665896982, 0.0)
    line15 = workPart.Curves.CreateLine(startPoint15, endPoint15)
    
    theSession.ActiveSketch.AddGeometry(line15, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_18 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_18.Geometry = line15
    conGeom1_18.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_18.SplineDefiningPointIndex = 0
    conGeom2_18 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_18.Geometry = line13
    conGeom2_18.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_18.SplineDefiningPointIndex = 0
    help9 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help9.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help9.Point.X = 178.13689126433937
    help9.Point.Y = 288.93362700339679
    help9.Point.Z = 0.0
    help9.Parameter = 0.0
    sketchHelpedGeometricConstraint11 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_18, conGeom2_18, help9)
    
    geom9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom9.Geometry = line15
    geom9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint23 = theSession.ActiveSketch.CreateVerticalConstraint(geom9)
    
    conGeom1_19 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_19.Geometry = line15
    conGeom1_19.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_19.SplineDefiningPointIndex = 0
    conGeom2_19 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_19.Geometry = line13
    conGeom2_19.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_19.SplineDefiningPointIndex = 0
    help10 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help10.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help10.Point.X = 178.13689126433934
    help10.Point.Y = 306.2180665896982
    help10.Point.Z = 0.0
    help10.Parameter = 0.0
    sketchHelpedGeometricConstraint12 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_19, conGeom2_19, help10)
    
    dimObject1_16 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_16.Geometry = line15
    dimObject1_16.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_16.AssocValue = 0
    dimObject1_16.HelpPoint.X = 0.0
    dimObject1_16.HelpPoint.Y = 0.0
    dimObject1_16.HelpPoint.Z = 0.0
    dimObject1_16.View = NXOpen.NXObject.Null
    dimObject2_14 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_14.Geometry = line15
    dimObject2_14.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_14.AssocValue = 0
    dimObject2_14.HelpPoint.X = 0.0
    dimObject2_14.HelpPoint.Y = 0.0
    dimObject2_14.HelpPoint.Z = 0.0
    dimObject2_14.View = NXOpen.NXObject.Null
    dimOrigin16 = NXOpen.Point3d(158.53878653656452, 297.57584679654741, 0.0)
    sketchDimensionalConstraint16 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_16, dimObject2_14, dimOrigin16, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint11 = sketchDimensionalConstraint16
    dimension16 = sketchHelpedDimensionalConstraint11.AssociatedDimension
    
    expression42 = sketchHelpedDimensionalConstraint11.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId110 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete21 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId111 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects10 = [NXOpen.TaggedObject.Null] * 6 
    objects10[0] = line14
    verticalDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 3 1")
    objects10[1] = verticalDimension1
    verticalDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    objects10[2] = verticalDimension2
    objects10[3] = line15
    parallelDimension1 = dimension16
    objects10[4] = parallelDimension1
    parallelDimension2 = dimension15
    objects10[5] = parallelDimension2
    nErrs22 = theSession.UpdateManager.AddObjectsToDeleteList(objects10)
    
    notifyOnDelete22 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id10 = theSession.NewestVisibleUndoMark
    
    nErrs23 = theSession.UpdateManager.DoUpdate(id10)
    
    theSession.DeleteUndoMark(markId110, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId112 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete23 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId113 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects11 = [NXOpen.TaggedObject.Null] * 1 
    objects11[0] = sketchGeometricConstraint21
    nErrs24 = theSession.UpdateManager.AddObjectsToDeleteList(objects11)
    
    notifyOnDelete24 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id11 = theSession.NewestVisibleUndoMark
    
    nErrs25 = theSession.UpdateManager.DoUpdate(id11)
    
    theSession.DeleteUndoMark(markId112, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId114 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete25 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId115 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects12 = [NXOpen.TaggedObject.Null] * 1 
    objects12[0] = line13
    nErrs26 = theSession.UpdateManager.AddObjectsToDeleteList(objects12)
    
    notifyOnDelete26 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id12 = theSession.NewestVisibleUndoMark
    
    nErrs27 = theSession.UpdateManager.DoUpdate(id12)
    
    theSession.DeleteUndoMark(markId114, None)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId116 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId117 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId117, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint16 = NXOpen.Point3d(171.79926341602899, 200.00000000000003, 0.0)
    endPoint16 = NXOpen.Point3d(171.79926341602891, 265.0, 0.0)
    line16 = workPart.Curves.CreateLine(startPoint16, endPoint16)
    
    theSession.ActiveSketch.AddGeometry(line16, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_20 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_20.Geometry = line16
    conGeom1_20.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_20.SplineDefiningPointIndex = 0
    conGeom2_20 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_20.Geometry = line3
    conGeom2_20.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_20.SplineDefiningPointIndex = 0
    help11 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help11.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help11.Point.X = 171.79926341602899
    help11.Point.Y = 200.00000000000003
    help11.Point.Z = 0.0
    help11.Parameter = 0.0
    sketchHelpedGeometricConstraint13 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_20, conGeom2_20, help11)
    
    geom10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom10.Geometry = line16
    geom10.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint24 = theSession.ActiveSketch.CreateVerticalConstraint(geom10)
    
    dimObject1_17 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_17.Geometry = line16
    dimObject1_17.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_17.AssocValue = 0
    dimObject1_17.HelpPoint.X = 0.0
    dimObject1_17.HelpPoint.Y = 0.0
    dimObject1_17.HelpPoint.Z = 0.0
    dimObject1_17.View = NXOpen.NXObject.Null
    dimObject2_15 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_15.Geometry = line16
    dimObject2_15.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_15.AssocValue = 0
    dimObject2_15.HelpPoint.X = 0.0
    dimObject2_15.HelpPoint.Y = 0.0
    dimObject2_15.HelpPoint.Z = 0.0
    dimObject2_15.View = NXOpen.NXObject.Null
    dimOrigin17 = NXOpen.Point3d(152.20115868825414, 232.49999999999997, 0.0)
    sketchDimensionalConstraint17 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_17, dimObject2_15, dimOrigin17, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint12 = sketchDimensionalConstraint17
    dimension17 = sketchHelpedDimensionalConstraint12.AssociatedDimension
    
    expression43 = sketchHelpedDimensionalConstraint12.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId118 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId118, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint17 = NXOpen.Point3d(249.00309356817522, 265.0, 0.0)
    endPoint17 = NXOpen.Point3d(249.00309356817513, 305.0, 0.0)
    line17 = workPart.Curves.CreateLine(startPoint17, endPoint17)
    
    theSession.ActiveSketch.AddGeometry(line17, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom11.Geometry = line17
    geom11.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom11.SplineDefiningPointIndex = 0
    sketchGeometricConstraint25 = theSession.ActiveSketch.CreateVerticalConstraint(geom11)
    
    dimObject1_18 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_18.Geometry = line17
    dimObject1_18.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_18.AssocValue = 0
    dimObject1_18.HelpPoint.X = 0.0
    dimObject1_18.HelpPoint.Y = 0.0
    dimObject1_18.HelpPoint.Z = 0.0
    dimObject1_18.View = NXOpen.NXObject.Null
    dimObject2_16 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_16.Geometry = line17
    dimObject2_16.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_16.AssocValue = 0
    dimObject2_16.HelpPoint.X = 0.0
    dimObject2_16.HelpPoint.Y = 0.0
    dimObject2_16.HelpPoint.Z = 0.0
    dimObject2_16.View = NXOpen.NXObject.Null
    dimOrigin18 = NXOpen.Point3d(229.40498884040036, 284.99999999999994, 0.0)
    sketchDimensionalConstraint18 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_18, dimObject2_16, dimOrigin18, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint13 = sketchDimensionalConstraint18
    dimension18 = sketchHelpedDimensionalConstraint13.AssociatedDimension
    
    expression44 = sketchHelpedDimensionalConstraint13.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId119 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId119, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint18 = NXOpen.Point3d(249.00309356817522, 265.0, 0.0)
    endPoint18 = NXOpen.Point3d(171.79926341602891, 265.0, 0.0)
    line18 = workPart.Curves.CreateLine(startPoint18, endPoint18)
    
    theSession.ActiveSketch.AddGeometry(line18, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_10.Geometry = line18
    geom1_10.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_10.SplineDefiningPointIndex = 0
    geom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_10.Geometry = line17
    geom2_10.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint26 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_10, geom2_10)
    
    geom12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom12.Geometry = line18
    geom12.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom12.SplineDefiningPointIndex = 0
    sketchGeometricConstraint27 = theSession.ActiveSketch.CreateHorizontalConstraint(geom12)
    
    geom1_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_11.Geometry = line18
    geom1_11.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_11.SplineDefiningPointIndex = 0
    geom2_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_11.Geometry = line16
    geom2_11.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_11.SplineDefiningPointIndex = 0
    sketchGeometricConstraint28 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_11, geom2_11)
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId120 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId120, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint19 = NXOpen.Point3d(249.00309356817513, 305.0, 0.0)
    endPoint19 = NXOpen.Point3d(210.40117849210205, 305.0, 0.0)
    line19 = workPart.Curves.CreateLine(startPoint19, endPoint19)
    
    theSession.ActiveSketch.AddGeometry(line19, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_12.Geometry = line19
    geom1_12.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_12.SplineDefiningPointIndex = 0
    geom2_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_12.Geometry = line17
    geom2_12.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_12.SplineDefiningPointIndex = 0
    sketchGeometricConstraint29 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_12, geom2_12)
    
    geom13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom13.Geometry = line19
    geom13.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint30 = theSession.ActiveSketch.CreateHorizontalConstraint(geom13)
    
    dimObject1_19 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_19.Geometry = line19
    dimObject1_19.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_19.AssocValue = 0
    dimObject1_19.HelpPoint.X = 0.0
    dimObject1_19.HelpPoint.Y = 0.0
    dimObject1_19.HelpPoint.Z = 0.0
    dimObject1_19.View = NXOpen.NXObject.Null
    dimObject2_17 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_17.Geometry = line19
    dimObject2_17.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_17.AssocValue = 0
    dimObject2_17.HelpPoint.X = 0.0
    dimObject2_17.HelpPoint.Y = 0.0
    dimObject2_17.HelpPoint.Z = 0.0
    dimObject2_17.View = NXOpen.NXObject.Null
    dimOrigin19 = NXOpen.Point3d(229.7021360301386, 285.40189527222515, 0.0)
    sketchDimensionalConstraint19 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_19, dimObject2_17, dimOrigin19, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint14 = sketchDimensionalConstraint19
    dimension19 = sketchHelpedDimensionalConstraint14.AssociatedDimension
    
    expression45 = sketchHelpedDimensionalConstraint14.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId121 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId121, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint20 = NXOpen.Point3d(210.40117849210205, 305.0, 0.0)
    endPoint20 = NXOpen.Point3d(210.40117849210208, 285.0, 0.0)
    line20 = workPart.Curves.CreateLine(startPoint20, endPoint20)
    
    theSession.ActiveSketch.AddGeometry(line20, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_13.Geometry = line20
    geom1_13.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_13.SplineDefiningPointIndex = 0
    geom2_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_13.Geometry = line19
    geom2_13.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint31 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_13, geom2_13)
    
    geom14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom14.Geometry = line20
    geom14.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom14.SplineDefiningPointIndex = 0
    sketchGeometricConstraint32 = theSession.ActiveSketch.CreateVerticalConstraint(geom14)
    
    dimObject1_20 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_20.Geometry = line20
    dimObject1_20.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_20.AssocValue = 0
    dimObject1_20.HelpPoint.X = 0.0
    dimObject1_20.HelpPoint.Y = 0.0
    dimObject1_20.HelpPoint.Z = 0.0
    dimObject1_20.View = NXOpen.NXObject.Null
    dimObject2_18 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_18.Geometry = line20
    dimObject2_18.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_18.AssocValue = 0
    dimObject2_18.HelpPoint.X = 0.0
    dimObject2_18.HelpPoint.Y = 0.0
    dimObject2_18.HelpPoint.Z = 0.0
    dimObject2_18.View = NXOpen.NXObject.Null
    dimOrigin20 = NXOpen.Point3d(229.9992832198769, 295.0, 0.0)
    sketchDimensionalConstraint20 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_20, dimObject2_18, dimOrigin20, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint15 = sketchDimensionalConstraint20
    dimension20 = sketchHelpedDimensionalConstraint15.AssociatedDimension
    
    expression46 = sketchHelpedDimensionalConstraint15.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId122 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId122, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint21 = NXOpen.Point3d(148.1771959814171, 285.0, 0.0)
    endPoint21 = NXOpen.Point3d(147.60104799520715, 200.00000000000003, 0.0)
    line21 = workPart.Curves.CreateLine(startPoint21, endPoint21)
    
    theSession.ActiveSketch.AddGeometry(line21, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_21 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_21.Geometry = line21
    conGeom1_21.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_21.SplineDefiningPointIndex = 0
    conGeom2_21 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_21.Geometry = line3
    conGeom2_21.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_21.SplineDefiningPointIndex = 0
    help12 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help12.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help12.Point.X = 147.60104799520704
    help12.Point.Y = 200.00000000000003
    help12.Point.Z = 0.0
    help12.Parameter = 0.0
    sketchHelpedGeometricConstraint14 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_21, conGeom2_21, help12)
    
    dimObject1_21 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_21.Geometry = line21
    dimObject1_21.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_21.AssocValue = 0
    dimObject1_21.HelpPoint.X = 0.0
    dimObject1_21.HelpPoint.Y = 0.0
    dimObject1_21.HelpPoint.Z = 0.0
    dimObject1_21.View = NXOpen.NXObject.Null
    dimObject2_19 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_19.Geometry = line21
    dimObject2_19.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_19.AssocValue = 0
    dimObject2_19.HelpPoint.X = 0.0
    dimObject2_19.HelpPoint.Y = 0.0
    dimObject2_19.HelpPoint.Z = 0.0
    dimObject2_19.View = NXOpen.NXObject.Null
    dimOrigin21 = NXOpen.Point3d(167.48677652244328, 242.36716295065554, 0.0)
    sketchDimensionalConstraint21 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_21, dimObject2_19, dimOrigin21, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint16 = sketchDimensionalConstraint21
    dimension21 = sketchHelpedDimensionalConstraint16.AssociatedDimension
    
    expression47 = sketchHelpedDimensionalConstraint16.AssociatedExpression
    
    dimObject1_22 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_22.Geometry = datumAxis2
    dimObject1_22.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject1_22.AssocValue = 0
    dimObject1_22.HelpPoint.X = -28.574999999999999
    dimObject1_22.HelpPoint.Y = 200.0
    dimObject1_22.HelpPoint.Z = 0.0
    dimObject1_22.View = NXOpen.NXObject.Null
    dimObject2_20 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_20.Geometry = line21
    dimObject2_20.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject2_20.AssocValue = 0
    dimObject2_20.HelpPoint.X = 148.1771959814171
    dimObject2_20.HelpPoint.Y = 285.0
    dimObject2_20.HelpPoint.Z = 0.0
    dimObject2_20.View = NXOpen.NXObject.Null
    dimOrigin22 = NXOpen.Point3d(133.79014008667249, 213.90483842634663, 0.0)
    sketchDimensionalConstraint22 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_22, dimObject2_20, dimOrigin22, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension22 = sketchDimensionalConstraint22.AssociatedDimension
    
    expression48 = sketchDimensionalConstraint22.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId123 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId123, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint22 = NXOpen.Point3d(210.40117849210208, 285.0, 0.0)
    endPoint22 = NXOpen.Point3d(147.88912198831213, 285.0, 0.0)
    line22 = workPart.Curves.CreateLine(startPoint22, endPoint22)
    
    theSession.ActiveSketch.AddGeometry(line22, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_14.Geometry = line22
    geom1_14.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_14.SplineDefiningPointIndex = 0
    geom2_14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_14.Geometry = line20
    geom2_14.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_14.SplineDefiningPointIndex = 0
    sketchGeometricConstraint33 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_14, geom2_14)
    
    geom15 = NXOpen.Sketch.ConstraintGeometry()
    
    geom15.Geometry = line22
    geom15.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom15.SplineDefiningPointIndex = 0
    sketchGeometricConstraint34 = theSession.ActiveSketch.CreateHorizontalConstraint(geom15)
    
    geom1_15 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_15.Geometry = line22
    geom1_15.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_15.SplineDefiningPointIndex = 0
    geom2_15 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_15.Geometry = line21
    geom2_15.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_15.SplineDefiningPointIndex = 0
    sketchGeometricConstraint35 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_15, geom2_15)
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId124 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId124, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint23 = NXOpen.Point3d(99.999999999999972, 285.0, 0.0)
    endPoint23 = NXOpen.Point3d(100.00000000000016, 200.0, 0.0)
    line23 = workPart.Curves.CreateLine(startPoint23, endPoint23)
    
    theSession.ActiveSketch.AddGeometry(line23, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom16 = NXOpen.Sketch.ConstraintGeometry()
    
    geom16.Geometry = line23
    geom16.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom16.SplineDefiningPointIndex = 0
    sketchGeometricConstraint36 = theSession.ActiveSketch.CreateVerticalConstraint(geom16)
    
    geom1_16 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_16.Geometry = line23
    geom1_16.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_16.SplineDefiningPointIndex = 0
    geom2_16 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_16.Geometry = line3
    geom2_16.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    geom2_16.SplineDefiningPointIndex = 0
    sketchGeometricConstraint37 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_16, geom2_16)
    
    dimObject1_23 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_23.Geometry = line23
    dimObject1_23.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_23.AssocValue = 0
    dimObject1_23.HelpPoint.X = 0.0
    dimObject1_23.HelpPoint.Y = 0.0
    dimObject1_23.HelpPoint.Z = 0.0
    dimObject1_23.View = NXOpen.NXObject.Null
    dimObject2_21 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_21.Geometry = line23
    dimObject2_21.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_21.AssocValue = 0
    dimObject2_21.HelpPoint.X = 0.0
    dimObject2_21.HelpPoint.Y = 0.0
    dimObject2_21.HelpPoint.Z = 0.0
    dimObject2_21.View = NXOpen.NXObject.Null
    dimOrigin23 = NXOpen.Point3d(119.59810472777488, 242.50000000000003, 0.0)
    sketchDimensionalConstraint23 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_23, dimObject2_21, dimOrigin23, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint17 = sketchDimensionalConstraint23
    dimension23 = sketchHelpedDimensionalConstraint17.AssociatedDimension
    
    expression49 = sketchHelpedDimensionalConstraint17.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId125 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId125, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint24 = NXOpen.Point3d(99.999999999999972, 285.0, 0.0)
    endPoint24 = NXOpen.Point3d(69.999999999999972, 285.0, 0.0)
    line24 = workPart.Curves.CreateLine(startPoint24, endPoint24)
    
    theSession.ActiveSketch.AddGeometry(line24, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_17 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_17.Geometry = line24
    geom1_17.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_17.SplineDefiningPointIndex = 0
    geom2_17 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_17.Geometry = line23
    geom2_17.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_17.SplineDefiningPointIndex = 0
    sketchGeometricConstraint38 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_17, geom2_17)
    
    geom17 = NXOpen.Sketch.ConstraintGeometry()
    
    geom17.Geometry = line24
    geom17.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom17.SplineDefiningPointIndex = 0
    sketchGeometricConstraint39 = theSession.ActiveSketch.CreateHorizontalConstraint(geom17)
    
    dimObject1_24 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_24.Geometry = line24
    dimObject1_24.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_24.AssocValue = 0
    dimObject1_24.HelpPoint.X = 0.0
    dimObject1_24.HelpPoint.Y = 0.0
    dimObject1_24.HelpPoint.Z = 0.0
    dimObject1_24.View = NXOpen.NXObject.Null
    dimObject2_22 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_22.Geometry = line24
    dimObject2_22.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_22.AssocValue = 0
    dimObject2_22.HelpPoint.X = 0.0
    dimObject2_22.HelpPoint.Y = 0.0
    dimObject2_22.HelpPoint.Z = 0.0
    dimObject2_22.View = NXOpen.NXObject.Null
    dimOrigin24 = NXOpen.Point3d(84.999999999999972, 265.40189527222515, 0.0)
    sketchDimensionalConstraint24 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_24, dimObject2_22, dimOrigin24, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint18 = sketchDimensionalConstraint24
    dimension24 = sketchHelpedDimensionalConstraint18.AssociatedDimension
    
    expression50 = sketchHelpedDimensionalConstraint18.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId126 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId126, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint25 = NXOpen.Point3d(70.97336582927079, 200.0, 0.0)
    endPoint25 = NXOpen.Point3d(70.973365829270705, 265.0, 0.0)
    line25 = workPart.Curves.CreateLine(startPoint25, endPoint25)
    
    theSession.ActiveSketch.AddGeometry(line25, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_22 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_22.Geometry = line25
    conGeom1_22.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_22.SplineDefiningPointIndex = 0
    conGeom2_22 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_22.Geometry = line3
    conGeom2_22.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_22.SplineDefiningPointIndex = 0
    help13 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help13.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help13.Point.X = 70.97336582927079
    help13.Point.Y = 200.0
    help13.Point.Z = 0.0
    help13.Parameter = 0.0
    sketchHelpedGeometricConstraint15 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_22, conGeom2_22, help13)
    
    geom18 = NXOpen.Sketch.ConstraintGeometry()
    
    geom18.Geometry = line25
    geom18.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom18.SplineDefiningPointIndex = 0
    sketchGeometricConstraint40 = theSession.ActiveSketch.CreateVerticalConstraint(geom18)
    
    dimObject1_25 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_25.Geometry = line25
    dimObject1_25.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_25.AssocValue = 0
    dimObject1_25.HelpPoint.X = 0.0
    dimObject1_25.HelpPoint.Y = 0.0
    dimObject1_25.HelpPoint.Z = 0.0
    dimObject1_25.View = NXOpen.NXObject.Null
    dimObject2_23 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_23.Geometry = line25
    dimObject2_23.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_23.AssocValue = 0
    dimObject2_23.HelpPoint.X = 0.0
    dimObject2_23.HelpPoint.Y = 0.0
    dimObject2_23.HelpPoint.Z = 0.0
    dimObject2_23.View = NXOpen.NXObject.Null
    dimOrigin25 = NXOpen.Point3d(51.375261101495923, 232.49999999999997, 0.0)
    sketchDimensionalConstraint25 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_25, dimObject2_23, dimOrigin25, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint19 = sketchDimensionalConstraint25
    dimension25 = sketchHelpedDimensionalConstraint19.AssociatedDimension
    
    expression51 = sketchHelpedDimensionalConstraint19.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId127 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId127, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint26 = NXOpen.Point3d(16.815455125526448, 265.0, 0.0)
    endPoint26 = NXOpen.Point3d(16.815455125526391, 310.0, 0.0)
    line26 = workPart.Curves.CreateLine(startPoint26, endPoint26)
    
    theSession.ActiveSketch.AddGeometry(line26, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom19 = NXOpen.Sketch.ConstraintGeometry()
    
    geom19.Geometry = line26
    geom19.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom19.SplineDefiningPointIndex = 0
    sketchGeometricConstraint41 = theSession.ActiveSketch.CreateVerticalConstraint(geom19)
    
    dimObject1_26 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_26.Geometry = line26
    dimObject1_26.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_26.AssocValue = 0
    dimObject1_26.HelpPoint.X = 0.0
    dimObject1_26.HelpPoint.Y = 0.0
    dimObject1_26.HelpPoint.Z = 0.0
    dimObject1_26.View = NXOpen.NXObject.Null
    dimObject2_24 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_24.Geometry = line26
    dimObject2_24.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_24.AssocValue = 0
    dimObject2_24.HelpPoint.X = 0.0
    dimObject2_24.HelpPoint.Y = 0.0
    dimObject2_24.HelpPoint.Z = 0.0
    dimObject2_24.View = NXOpen.NXObject.Null
    dimOrigin26 = NXOpen.Point3d(-2.7826496022484086, 287.5, 0.0)
    sketchDimensionalConstraint26 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_26, dimObject2_24, dimOrigin26, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint20 = sketchDimensionalConstraint26
    dimension26 = sketchHelpedDimensionalConstraint20.AssociatedDimension
    
    expression52 = sketchHelpedDimensionalConstraint20.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId128 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId128, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint27 = NXOpen.Point3d(16.815455125526391, 310.0, 0.0)
    endPoint27 = NXOpen.Point3d(41.754556382021988, 310.0, 0.0)
    line27 = workPart.Curves.CreateLine(startPoint27, endPoint27)
    
    theSession.ActiveSketch.AddGeometry(line27, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_18 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_18.Geometry = line27
    geom1_18.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_18.SplineDefiningPointIndex = 0
    geom2_18 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_18.Geometry = line26
    geom2_18.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_18.SplineDefiningPointIndex = 0
    sketchGeometricConstraint42 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_18, geom2_18)
    
    geom20 = NXOpen.Sketch.ConstraintGeometry()
    
    geom20.Geometry = line27
    geom20.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom20.SplineDefiningPointIndex = 0
    sketchGeometricConstraint43 = theSession.ActiveSketch.CreateHorizontalConstraint(geom20)
    
    dimObject1_27 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_27.Geometry = line27
    dimObject1_27.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_27.AssocValue = 0
    dimObject1_27.HelpPoint.X = 0.0
    dimObject1_27.HelpPoint.Y = 0.0
    dimObject1_27.HelpPoint.Z = 0.0
    dimObject1_27.View = NXOpen.NXObject.Null
    dimObject2_25 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_25.Geometry = line27
    dimObject2_25.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_25.AssocValue = 0
    dimObject2_25.HelpPoint.X = 0.0
    dimObject2_25.HelpPoint.Y = 0.0
    dimObject2_25.HelpPoint.Z = 0.0
    dimObject2_25.View = NXOpen.NXObject.Null
    dimOrigin27 = NXOpen.Point3d(29.28500575377419, 329.59810472777485, 0.0)
    sketchDimensionalConstraint27 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_27, dimObject2_25, dimOrigin27, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint21 = sketchDimensionalConstraint27
    dimension27 = sketchHelpedDimensionalConstraint21.AssociatedDimension
    
    expression53 = sketchHelpedDimensionalConstraint21.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId129 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId129, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint28 = NXOpen.Point3d(41.754556382021988, 310.0, 0.0)
    endPoint28 = NXOpen.Point3d(41.754556382021988, 287.5, 0.0)
    line28 = workPart.Curves.CreateLine(startPoint28, endPoint28)
    
    theSession.ActiveSketch.AddGeometry(line28, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_19 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_19.Geometry = line28
    geom1_19.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_19.SplineDefiningPointIndex = 0
    geom2_19 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_19.Geometry = line27
    geom2_19.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_19.SplineDefiningPointIndex = 0
    sketchGeometricConstraint44 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_19, geom2_19)
    
    geom21 = NXOpen.Sketch.ConstraintGeometry()
    
    geom21.Geometry = line28
    geom21.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom21.SplineDefiningPointIndex = 0
    sketchGeometricConstraint45 = theSession.ActiveSketch.CreateVerticalConstraint(geom21)
    
    dimObject1_28 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_28.Geometry = line28
    dimObject1_28.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_28.AssocValue = 0
    dimObject1_28.HelpPoint.X = 0.0
    dimObject1_28.HelpPoint.Y = 0.0
    dimObject1_28.HelpPoint.Z = 0.0
    dimObject1_28.View = NXOpen.NXObject.Null
    dimObject2_26 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_26.Geometry = line28
    dimObject2_26.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_26.AssocValue = 0
    dimObject2_26.HelpPoint.X = 0.0
    dimObject2_26.HelpPoint.Y = 0.0
    dimObject2_26.HelpPoint.Z = 0.0
    dimObject2_26.View = NXOpen.NXObject.Null
    dimOrigin28 = NXOpen.Point3d(61.352661109796813, 298.75, 0.0)
    sketchDimensionalConstraint28 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_28, dimObject2_26, dimOrigin28, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint22 = sketchDimensionalConstraint28
    dimension28 = sketchHelpedDimensionalConstraint22.AssociatedDimension
    
    expression54 = sketchHelpedDimensionalConstraint22.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    scaleAboutPoint38 = NXOpen.Point3d(19.589031531141703, 103.13048953159841, 0.0)
    viewCenter38 = NXOpen.Point3d(-19.589031531141408, -103.13048953159831, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(15.671225224913403, 82.504391625278785, 0.0)
    viewCenter39 = NXOpen.Point3d(-15.671225224913089, -82.504391625278586, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(12.536980179930753, 66.003513300223048, 0.0)
    viewCenter40 = NXOpen.Point3d(-12.536980179930438, -66.003513300222863, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(10.029584143944653, 52.802810640178464, 0.0)
    viewCenter41 = NXOpen.Point3d(-10.029584143944327, -52.802810640178244, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(8.0236673151557625, 42.242248512142815, 0.0)
    viewCenter42 = NXOpen.Point3d(-8.0236673151554196, -42.242248512142574, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint42, viewCenter42)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId130 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete27 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId131 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects13 = [NXOpen.TaggedObject.Null] * 1 
    objects13[0] = line24
    nErrs28 = theSession.UpdateManager.AddObjectsToDeleteList(objects13)
    
    notifyOnDelete28 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id13 = theSession.NewestVisibleUndoMark
    
    nErrs29 = theSession.UpdateManager.DoUpdate(id13)
    
    theSession.DeleteUndoMark(markId130, None)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId132 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId133 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId133, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint29 = NXOpen.Point3d(99.999999999999972, 285.0, 0.0)
    endPoint29 = NXOpen.Point3d(41.754556382021988, 285.0, 0.0)
    line29 = workPart.Curves.CreateLine(startPoint29, endPoint29)
    
    theSession.ActiveSketch.AddGeometry(line29, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_20 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_20.Geometry = line29
    geom1_20.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_20.SplineDefiningPointIndex = 0
    geom2_20 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_20.Geometry = line23
    geom2_20.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_20.SplineDefiningPointIndex = 0
    sketchGeometricConstraint46 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_20, geom2_20)
    
    geom22 = NXOpen.Sketch.ConstraintGeometry()
    
    geom22.Geometry = line29
    geom22.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom22.SplineDefiningPointIndex = 0
    sketchGeometricConstraint47 = theSession.ActiveSketch.CreateHorizontalConstraint(geom22)
    
    dimObject1_29 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_29.Geometry = line29
    dimObject1_29.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_29.AssocValue = 0
    dimObject1_29.HelpPoint.X = 0.0
    dimObject1_29.HelpPoint.Y = 0.0
    dimObject1_29.HelpPoint.Z = 0.0
    dimObject1_29.View = NXOpen.NXObject.Null
    dimObject2_27 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_27.Geometry = line29
    dimObject2_27.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_27.AssocValue = 0
    dimObject2_27.HelpPoint.X = 0.0
    dimObject2_27.HelpPoint.Y = 0.0
    dimObject2_27.HelpPoint.Z = 0.0
    dimObject2_27.View = NXOpen.NXObject.Null
    dimOrigin29 = NXOpen.Point3d(70.877278191010987, 278.57809304280272, 0.0)
    sketchDimensionalConstraint29 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_29, dimObject2_27, dimOrigin29, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint23 = sketchDimensionalConstraint29
    dimension29 = sketchHelpedDimensionalConstraint23.AssociatedDimension
    
    expression55 = sketchHelpedDimensionalConstraint23.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId134 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete29 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId135 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects14 = [NXOpen.TaggedObject.Null] * 1 
    objects14[0] = line28
    nErrs30 = theSession.UpdateManager.AddObjectsToDeleteList(objects14)
    
    notifyOnDelete30 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id14 = theSession.NewestVisibleUndoMark
    
    nErrs31 = theSession.UpdateManager.DoUpdate(id14)
    
    theSession.DeleteUndoMark(markId134, None)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId136 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId137 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId137, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint30 = NXOpen.Point3d(41.754556382021988, 310.0, 0.0)
    endPoint30 = NXOpen.Point3d(41.754556382022038, 285.0, 0.0)
    line30 = workPart.Curves.CreateLine(startPoint30, endPoint30)
    
    theSession.ActiveSketch.AddGeometry(line30, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_21 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_21.Geometry = line30
    geom1_21.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_21.SplineDefiningPointIndex = 0
    geom2_21 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_21.Geometry = line27
    geom2_21.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_21.SplineDefiningPointIndex = 0
    sketchGeometricConstraint48 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_21, geom2_21)
    
    geom23 = NXOpen.Sketch.ConstraintGeometry()
    
    geom23.Geometry = line30
    geom23.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom23.SplineDefiningPointIndex = 0
    sketchGeometricConstraint49 = theSession.ActiveSketch.CreateVerticalConstraint(geom23)
    
    geom1_22 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_22.Geometry = line30
    geom1_22.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_22.SplineDefiningPointIndex = 0
    geom2_22 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_22.Geometry = line29
    geom2_22.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_22.SplineDefiningPointIndex = 0
    sketchGeometricConstraint50 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_22, geom2_22)
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId138 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete31 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId139 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects15 = [NXOpen.TaggedObject.Null] * 1 
    objects15[0] = line26
    nErrs32 = theSession.UpdateManager.AddObjectsToDeleteList(objects15)
    
    notifyOnDelete32 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id15 = theSession.NewestVisibleUndoMark
    
    nErrs33 = theSession.UpdateManager.DoUpdate(id15)
    
    theSession.DeleteUndoMark(markId138, None)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId140 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId141 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    markId142 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId142, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint31 = NXOpen.Point3d(70.973365829270705, 265.0, 0.0)
    endPoint31 = NXOpen.Point3d(16.815455125526395, 265.0, 0.0)
    line31 = workPart.Curves.CreateLine(startPoint31, endPoint31)
    
    theSession.ActiveSketch.AddGeometry(line31, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_23 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_23.Geometry = line31
    geom1_23.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_23.SplineDefiningPointIndex = 0
    geom2_23 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_23.Geometry = line25
    geom2_23.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_23.SplineDefiningPointIndex = 0
    sketchGeometricConstraint51 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_23, geom2_23)
    
    geom24 = NXOpen.Sketch.ConstraintGeometry()
    
    geom24.Geometry = line31
    geom24.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom24.SplineDefiningPointIndex = 0
    sketchGeometricConstraint52 = theSession.ActiveSketch.CreateHorizontalConstraint(geom24)
    
    dimObject1_30 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_30.Geometry = line31
    dimObject1_30.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_30.AssocValue = 0
    dimObject1_30.HelpPoint.X = 0.0
    dimObject1_30.HelpPoint.Y = 0.0
    dimObject1_30.HelpPoint.Z = 0.0
    dimObject1_30.View = NXOpen.NXObject.Null
    dimObject2_28 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_28.Geometry = line31
    dimObject2_28.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_28.AssocValue = 0
    dimObject2_28.HelpPoint.X = 0.0
    dimObject2_28.HelpPoint.Y = 0.0
    dimObject2_28.HelpPoint.Z = 0.0
    dimObject2_28.View = NXOpen.NXObject.Null
    dimOrigin30 = NXOpen.Point3d(43.894410477398552, 258.57809304280272, 0.0)
    sketchDimensionalConstraint30 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_30, dimObject2_28, dimOrigin30, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint24 = sketchDimensionalConstraint30
    dimension30 = sketchHelpedDimensionalConstraint24.AssociatedDimension
    
    expression56 = sketchHelpedDimensionalConstraint24.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    markId143 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId143, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint32 = NXOpen.Point3d(16.815455125526391, 310.0, 0.0)
    endPoint32 = NXOpen.Point3d(16.815455125526483, 265.0, 0.0)
    line32 = workPart.Curves.CreateLine(startPoint32, endPoint32)
    
    theSession.ActiveSketch.AddGeometry(line32, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_24 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_24.Geometry = line32
    geom1_24.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_24.SplineDefiningPointIndex = 0
    geom2_24 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_24.Geometry = line27
    geom2_24.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_24.SplineDefiningPointIndex = 0
    sketchGeometricConstraint53 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_24, geom2_24)
    
    geom25 = NXOpen.Sketch.ConstraintGeometry()
    
    geom25.Geometry = line32
    geom25.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom25.SplineDefiningPointIndex = 0
    sketchGeometricConstraint54 = theSession.ActiveSketch.CreateVerticalConstraint(geom25)
    
    geom1_25 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_25.Geometry = line32
    geom1_25.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_25.SplineDefiningPointIndex = 0
    geom2_25 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_25.Geometry = line31
    geom2_25.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_25.SplineDefiningPointIndex = 0
    sketchGeometricConstraint55 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_25, geom2_25)
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    scaleAboutPoint43 = NXOpen.Point3d(24.542982375770201, -8.4956477454587507, 0.0)
    viewCenter43 = NXOpen.Point3d(-24.542982375769881, 8.4956477454589763, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(30.678727969712732, -10.619559681823459, 0.0)
    viewCenter44 = NXOpen.Point3d(-30.678727969712387, 10.6195596818237, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(39.528361037899074, -13.569437371218902, 0.0)
    viewCenter45 = NXOpen.Point3d(-39.528361037898698, 13.569437371219102, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(49.410451297373704, -16.961796714023652, 0.0)
    viewCenter46 = NXOpen.Point3d(-49.410451297373264, 16.961796714023812, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint46, viewCenter46)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖約束(K)->尺寸(D)->快速(P)...
    # ----------------------------------------------
    markId144 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder13 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines61 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBefore(lines61)
    
    lines62 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAfter(lines62)
    
    lines63 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAbove(lines63)
    
    lines64 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBelow(lines64)
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder13.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines65 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBefore(lines65)
    
    lines66 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAfter(lines66)
    
    lines67 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAbove(lines67)
    
    lines68 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBelow(lines68)
    
    theSession.SetUndoMarkName(markId144, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder13.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits319 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits320 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits321 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits322 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits323 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits324 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits325 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits326 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits327 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits328 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder13.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder13.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits329 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits330 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits331 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits332 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits333 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits334 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits335 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits336 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits337 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits338 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    point31 = NXOpen.Point3d(171.79926341602896, 215.92857900739355, 0.0)
    sketchRapidDimensionBuilder13.FirstAssociativity.SetValue(line16, workPart.ModelingViews.WorkView, point31)
    
    point1_28 = NXOpen.Point3d(171.79926341602899, 200.00000000000003, 0.0)
    point2_28 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line16, workPart.ModelingViews.WorkView, point1_28, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_28)
    
    point1_29 = NXOpen.Point3d(171.79926341602891, 265.0, 0.0)
    point2_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line16, workPart.ModelingViews.WorkView, point1_29, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_29)
    
    dimensionlinearunits339 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits340 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits341 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits342 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits343 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits344 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    point32 = NXOpen.Point3d(147.72471781751744, 218.2451994070577, 0.0)
    sketchRapidDimensionBuilder13.SecondAssociativity.SetValue(line21, workPart.ModelingViews.WorkView, point32)
    
    point1_30 = NXOpen.Point3d(171.79926341602896, 215.92857900739355, 0.0)
    point2_30 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line16, workPart.ModelingViews.WorkView, point1_30, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_30)
    
    point1_31 = NXOpen.Point3d(147.72471781751744, 218.2451994070577, 0.0)
    point2_31 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line21, workPart.ModelingViews.WorkView, point1_31, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_31)
    
    point1_32 = NXOpen.Point3d(171.79926341602896, 215.92857900739355, 0.0)
    point2_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line16, workPart.ModelingViews.WorkView, point1_32, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_32)
    
    point1_33 = NXOpen.Point3d(147.72471781751744, 218.2451994070577, 0.0)
    point2_33 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line21, workPart.ModelingViews.WorkView, point1_33, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_33)
    
    dimensionlinearunits345 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits346 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits347 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits348 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits349 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits350 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin10 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin10.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin10.View = NXOpen.View.Null
    assocOrigin10.ViewOfGeometry = workPart.ModelingViews.WorkView
    point33 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin10.PointOnGeometry = point33
    assocOrigin10.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin10.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin10.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.DimensionLine = 0
    assocOrigin10.AssociatedView = NXOpen.View.Null
    assocOrigin10.AssociatedPoint = NXOpen.Point.Null
    assocOrigin10.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin10.XOffsetFactor = 0.0
    assocOrigin10.YOffsetFactor = 0.0
    assocOrigin10.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder13.Origin.SetAssociativeOrigin(assocOrigin10)
    
    point34 = NXOpen.Point3d(159.63949884562984, 218.69408934120176, 0.0)
    sketchRapidDimensionBuilder13.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point34)
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder13.Style.DimensionStyle.TextCentered = False
    
    markId145 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject13 = sketchRapidDimensionBuilder13.Commit()
    
    theSession.DeleteUndoMark(markId145, None)
    
    theSession.SetUndoMarkName(markId144, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId144, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder13.Destroy()
    
    markId146 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder14 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines69 = []
    sketchRapidDimensionBuilder14.AppendedText.SetBefore(lines69)
    
    lines70 = []
    sketchRapidDimensionBuilder14.AppendedText.SetAfter(lines70)
    
    lines71 = []
    sketchRapidDimensionBuilder14.AppendedText.SetAbove(lines71)
    
    lines72 = []
    sketchRapidDimensionBuilder14.AppendedText.SetBelow(lines72)
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder14.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder14.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder14.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder14.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId146, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder14.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits351 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits352 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits353 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits354 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits355 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits356 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits357 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits358 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits359 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits360 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder14.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder14.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder14.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits361 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits362 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits363 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits364 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits365 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits366 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits367 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits368 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits369 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits370 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    expression57 = workPart.Expressions.FindObject("p18")
    expression57.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId146, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId147 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId147, None)
    
    markId148 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId146, "Edit Driving Value")
    
    sketchRapidDimensionBuilder14.Destroy()
    
    theSession.UndoToMark(markId148, None)
    
    theSession.DeleteUndoMark(markId148, None)
    
    sketchRapidDimensionBuilder14.Destroy()
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId149 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete33 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId150 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects16 = [NXOpen.TaggedObject.Null] * 1 
    objects16[0] = line21
    nErrs34 = theSession.UpdateManager.AddObjectsToDeleteList(objects16)
    
    notifyOnDelete34 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id16 = theSession.NewestVisibleUndoMark
    
    nErrs35 = theSession.UpdateManager.DoUpdate(id16)
    
    theSession.DeleteUndoMark(markId149, None)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId151 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId152 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId152, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint33 = NXOpen.Point3d(151.93181542290773, 279.87570761442402, 0.0)
    endPoint33 = NXOpen.Point3d(151.9318154229079, 200.00000000000003, 0.0)
    line33 = workPart.Curves.CreateLine(startPoint33, endPoint33)
    
    theSession.ActiveSketch.AddGeometry(line33, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_26 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_26.Geometry = line33
    geom1_26.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_26.SplineDefiningPointIndex = 0
    geom2_26 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_26.Geometry = line22
    geom2_26.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_26.SplineDefiningPointIndex = 0
    sketchGeometricConstraint56 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_26, geom2_26)
    
    conGeom1_23 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_23.Geometry = line33
    conGeom1_23.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_23.SplineDefiningPointIndex = 0
    conGeom2_23 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_23.Geometry = line3
    conGeom2_23.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_23.SplineDefiningPointIndex = 0
    help14 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help14.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help14.Point.X = 152.26480462214124
    help14.Point.Y = 200.00000000000003
    help14.Point.Z = 0.0
    help14.Parameter = 0.0
    sketchHelpedGeometricConstraint16 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_23, conGeom2_23, help14)
    
    geom26 = NXOpen.Sketch.ConstraintGeometry()
    
    geom26.Geometry = line33
    geom26.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom26.SplineDefiningPointIndex = 0
    sketchGeometricConstraint57 = theSession.ActiveSketch.CreateVerticalConstraint(geom26)
    
    dimObject1_31 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_31.Geometry = line33
    dimObject1_31.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_31.AssocValue = 0
    dimObject1_31.HelpPoint.X = 0.0
    dimObject1_31.HelpPoint.Y = 0.0
    dimObject1_31.HelpPoint.Z = 0.0
    dimObject1_31.View = NXOpen.NXObject.Null
    dimObject2_29 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_29.Geometry = line33
    dimObject2_29.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_29.AssocValue = 0
    dimObject2_29.HelpPoint.X = 0.0
    dimObject2_29.HelpPoint.Y = 0.0
    dimObject2_29.HelpPoint.Z = 0.0
    dimObject2_29.View = NXOpen.NXObject.Null
    dimOrigin31 = NXOpen.Point3d(167.61029920512766, 239.93785380721206, 0.0)
    sketchDimensionalConstraint31 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_31, dimObject2_29, dimOrigin31, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint25 = sketchDimensionalConstraint31
    dimension31 = sketchHelpedDimensionalConstraint25.AssociatedDimension
    
    expression58 = sketchHelpedDimensionalConstraint25.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->草圖約束(K)->尺寸(D)->快速(P)...
    # ----------------------------------------------
    markId153 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder15 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines73 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBefore(lines73)
    
    lines74 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAfter(lines74)
    
    lines75 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAbove(lines75)
    
    lines76 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBelow(lines76)
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder15.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines77 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBefore(lines77)
    
    lines78 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAfter(lines78)
    
    lines79 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAbove(lines79)
    
    lines80 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBelow(lines80)
    
    theSession.SetUndoMarkName(markId153, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder15.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits371 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits372 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits373 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits374 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits375 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits376 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits377 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits378 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits379 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits380 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder15.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder15.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits381 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits382 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits383 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits384 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits385 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits386 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits387 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits388 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits389 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits390 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    point35 = NXOpen.Point3d(171.79926341602896, 218.69408934120176, 0.0)
    sketchRapidDimensionBuilder15.FirstAssociativity.SetValue(line16, workPart.ModelingViews.WorkView, point35)
    
    point1_34 = NXOpen.Point3d(171.79926341602899, 200.00000000000003, 0.0)
    point2_34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line16, workPart.ModelingViews.WorkView, point1_34, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_34)
    
    point1_35 = NXOpen.Point3d(171.79926341602891, 265.0, 0.0)
    point2_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line16, workPart.ModelingViews.WorkView, point1_35, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_35)
    
    dimensionlinearunits391 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits392 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits393 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits394 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits395 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits396 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    point1_36 = NXOpen.Point3d(151.9318154229079, 200.00000000000003, 0.0)
    point2_36 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line33, workPart.ModelingViews.WorkView, point1_36, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_36)
    
    point1_37 = NXOpen.Point3d(171.79926341602896, 218.69408934120176, 0.0)
    point2_37 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line16, workPart.ModelingViews.WorkView, point1_37, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_37)
    
    point1_38 = NXOpen.Point3d(151.9318154229079, 200.00000000000003, 0.0)
    point2_38 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line33, workPart.ModelingViews.WorkView, point1_38, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_38)
    
    point1_39 = NXOpen.Point3d(171.79926341602896, 218.69408934120176, 0.0)
    point2_39 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line16, workPart.ModelingViews.WorkView, point1_39, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_39)
    
    point1_40 = NXOpen.Point3d(151.9318154229079, 200.00000000000003, 0.0)
    point2_40 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line33, workPart.ModelingViews.WorkView, point1_40, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_40)
    
    dimensionlinearunits397 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits398 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits399 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits400 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits401 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits402 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits403 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits404 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits405 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits406 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits407 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits408 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin11 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin11.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin11.View = NXOpen.View.Null
    assocOrigin11.ViewOfGeometry = workPart.ModelingViews.WorkView
    point36 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin11.PointOnGeometry = point36
    assocOrigin11.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin11.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin11.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.DimensionLine = 0
    assocOrigin11.AssociatedView = NXOpen.View.Null
    assocOrigin11.AssociatedPoint = NXOpen.Point.Null
    assocOrigin11.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin11.XOffsetFactor = 0.0
    assocOrigin11.YOffsetFactor = 0.0
    assocOrigin11.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder15.Origin.SetAssociativeOrigin(assocOrigin11)
    
    point37 = NXOpen.Point3d(158.25674367872571, 320.55705330313799, 0.0)
    sketchRapidDimensionBuilder15.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point37)
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder15.Style.DimensionStyle.TextCentered = False
    
    markId154 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject14 = sketchRapidDimensionBuilder15.Commit()
    
    theSession.DeleteUndoMark(markId154, None)
    
    theSession.SetUndoMarkName(markId153, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId153, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder15.Destroy()
    
    markId155 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder16 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines81 = []
    sketchRapidDimensionBuilder16.AppendedText.SetBefore(lines81)
    
    lines82 = []
    sketchRapidDimensionBuilder16.AppendedText.SetAfter(lines82)
    
    lines83 = []
    sketchRapidDimensionBuilder16.AppendedText.SetAbove(lines83)
    
    lines84 = []
    sketchRapidDimensionBuilder16.AppendedText.SetBelow(lines84)
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder16.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId155, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder16.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits409 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits410 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits411 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits412 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits413 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits414 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits415 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits416 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits417 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits418 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder16.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits419 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits420 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits421 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits422 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits423 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits424 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits425 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits426 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits427 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits428 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    expression59 = workPart.Expressions.FindObject("p18")
    expression59.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId155, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId156 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId156, None)
    
    markId157 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId155, "Edit Driving Value")
    
    expression59.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId157, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId158 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId158, None)
    
    markId159 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId157, "Edit Driving Value")
    
    point38 = NXOpen.Point3d(252.75771300966568, 292.90194996505579, 0.0)
    sketchRapidDimensionBuilder16.FirstAssociativity.SetValue(line17, workPart.ModelingViews.WorkView, point38)
    
    point1_41 = NXOpen.Point3d(252.75771300966568, 299.87570761442402, 0.0)
    point2_41 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder16.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line17, workPart.ModelingViews.WorkView, point1_41, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_41)
    
    point1_42 = NXOpen.Point3d(252.75771300966568, 265.0, 0.0)
    point2_42 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder16.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line17, workPart.ModelingViews.WorkView, point1_42, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_42)
    
    dimensionlinearunits429 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits430 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits431 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits432 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits433 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits434 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    point1_43 = NXOpen.Point3d(214.02324592671394, 289.87570761442402, 0.0)
    point2_43 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder16.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line20, workPart.ModelingViews.WorkView, point1_43, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_43)
    
    point1_44 = NXOpen.Point3d(252.75771300966568, 292.90194996505579, 0.0)
    point2_44 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder16.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line17, workPart.ModelingViews.WorkView, point1_44, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_44)
    
    point1_45 = NXOpen.Point3d(214.02324592671394, 289.87570761442402, 0.0)
    point2_45 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder16.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line20, workPart.ModelingViews.WorkView, point1_45, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_45)
    
    point1_46 = NXOpen.Point3d(252.75771300966568, 292.90194996505579, 0.0)
    point2_46 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder16.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line17, workPart.ModelingViews.WorkView, point1_46, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_46)
    
    point1_47 = NXOpen.Point3d(214.02324592671394, 289.87570761442402, 0.0)
    point2_47 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder16.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line20, workPart.ModelingViews.WorkView, point1_47, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_47)
    
    dimensionlinearunits435 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits436 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits437 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits438 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits439 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits440 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits441 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits442 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits443 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits444 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits445 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits446 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin12 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin12.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin12.View = NXOpen.View.Null
    assocOrigin12.ViewOfGeometry = workPart.ModelingViews.WorkView
    point39 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin12.PointOnGeometry = point39
    assocOrigin12.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin12.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin12.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.DimensionLine = 0
    assocOrigin12.AssociatedView = NXOpen.View.Null
    assocOrigin12.AssociatedPoint = NXOpen.Point.Null
    assocOrigin12.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin12.XOffsetFactor = 0.0
    assocOrigin12.YOffsetFactor = 0.0
    assocOrigin12.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder16.Origin.SetAssociativeOrigin(assocOrigin12)
    
    point40 = NXOpen.Point3d(231.54276752464364, 330.23633947146681, 0.0)
    sketchRapidDimensionBuilder16.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point40)
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.TextCentered = True
    
    markId160 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject15 = sketchRapidDimensionBuilder16.Commit()
    
    theSession.DeleteUndoMark(markId160, None)
    
    theSession.SetUndoMarkName(markId159, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId159, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder16.Destroy()
    
    markId161 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder17 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines85 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBefore(lines85)
    
    lines86 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAfter(lines86)
    
    lines87 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAbove(lines87)
    
    lines88 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBelow(lines88)
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder17.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder17.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder17.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId161, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder17.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits447 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits448 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits449 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits450 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits451 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits452 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits453 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits454 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits455 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits456 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder17.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder17.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits457 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits458 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits459 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits460 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits461 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits462 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits463 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits464 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits465 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits466 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    expression60 = workPart.Expressions.FindObject("p19")
    expression60.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId161, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId162 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId162, None)
    
    markId163 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId161, "Edit Driving Value")
    
    point41 = NXOpen.Point3d(196.97388835204086, 279.87570761442396, 0.0)
    sketchRapidDimensionBuilder17.FirstAssociativity.SetValue(line22, workPart.ModelingViews.WorkView, point41)
    
    point1_48 = NXOpen.Point3d(214.02324592671394, 279.87570761442402, 0.0)
    point2_48 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line22, workPart.ModelingViews.WorkView, point1_48, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_48)
    
    point1_49 = NXOpen.Point3d(151.79926341602908, 279.87570761442402, 0.0)
    point2_49 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line22, workPart.ModelingViews.WorkView, point1_49, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_49)
    
    dimensionlinearunits467 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits468 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits469 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits470 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits471 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits472 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    point1_50 = NXOpen.Point3d(202.91125467137141, 265.0, 0.0)
    point2_50 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line18, workPart.ModelingViews.WorkView, point1_50, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_50)
    
    point1_51 = NXOpen.Point3d(196.97388835204086, 279.87570761442396, 0.0)
    point2_51 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line22, workPart.ModelingViews.WorkView, point1_51, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_51)
    
    point1_52 = NXOpen.Point3d(202.91125467137141, 265.0, 0.0)
    point2_52 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line18, workPart.ModelingViews.WorkView, point1_52, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_52)
    
    point1_53 = NXOpen.Point3d(196.97388835204086, 279.87570761442396, 0.0)
    point2_53 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line22, workPart.ModelingViews.WorkView, point1_53, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_53)
    
    point1_54 = NXOpen.Point3d(202.91125467137141, 265.0, 0.0)
    point2_54 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line18, workPart.ModelingViews.WorkView, point1_54, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_54)
    
    dimensionlinearunits473 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits474 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits475 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits476 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits477 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits478 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits479 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits480 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits481 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits482 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits483 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits484 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin13 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin13.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin13.View = NXOpen.View.Null
    assocOrigin13.ViewOfGeometry = workPart.ModelingViews.WorkView
    point42 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin13.PointOnGeometry = point42
    assocOrigin13.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin13.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin13.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.DimensionLine = 0
    assocOrigin13.AssociatedView = NXOpen.View.Null
    assocOrigin13.AssociatedPoint = NXOpen.Point.Null
    assocOrigin13.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin13.XOffsetFactor = 0.0
    assocOrigin13.YOffsetFactor = 0.0
    assocOrigin13.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder17.Origin.SetAssociativeOrigin(assocOrigin13)
    
    point43 = NXOpen.Point3d(224.62899169012312, 242.66184556753973, 0.0)
    sketchRapidDimensionBuilder17.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point43)
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder17.Style.DimensionStyle.TextCentered = False
    
    markId164 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject16 = sketchRapidDimensionBuilder17.Commit()
    
    theSession.DeleteUndoMark(markId164, None)
    
    theSession.SetUndoMarkName(markId163, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId163, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder17.Destroy()
    
    markId165 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder18 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines89 = []
    sketchRapidDimensionBuilder18.AppendedText.SetBefore(lines89)
    
    lines90 = []
    sketchRapidDimensionBuilder18.AppendedText.SetAfter(lines90)
    
    lines91 = []
    sketchRapidDimensionBuilder18.AppendedText.SetAbove(lines91)
    
    lines92 = []
    sketchRapidDimensionBuilder18.AppendedText.SetBelow(lines92)
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder18.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId165, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder18.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits485 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits486 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits487 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits488 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits489 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits490 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits491 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits492 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits493 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits494 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder18.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits495 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits496 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits497 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits498 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits499 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits500 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits501 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits502 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits503 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits504 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    expression61 = workPart.Expressions.FindObject("p20")
    expression61.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId165, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId166 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId166, None)
    
    markId167 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId165, "Edit Driving Value")
    
    point44 = NXOpen.Point3d(100.00000000000011, 224.22511000881821, 0.0)
    sketchRapidDimensionBuilder18.FirstAssociativity.SetValue(line23, workPart.ModelingViews.WorkView, point44)
    
    point1_55 = NXOpen.Point3d(100.00000000000016, 200.0, 0.0)
    point2_55 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line23, workPart.ModelingViews.WorkView, point1_55, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_55)
    
    point1_56 = NXOpen.Point3d(99.999999999999972, 285.0, 0.0)
    point2_56 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line23, workPart.ModelingViews.WorkView, point1_56, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_56)
    
    dimensionlinearunits505 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits506 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits507 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits508 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits509 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits510 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    point1_57 = NXOpen.Point3d(70.973365829270747, 232.5, 0.0)
    point2_57 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line25, workPart.ModelingViews.WorkView, point1_57, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_57)
    
    point1_58 = NXOpen.Point3d(100.00000000000011, 224.22511000881821, 0.0)
    point2_58 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line23, workPart.ModelingViews.WorkView, point1_58, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_58)
    
    point1_59 = NXOpen.Point3d(70.973365829270747, 232.5, 0.0)
    point2_59 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line25, workPart.ModelingViews.WorkView, point1_59, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_59)
    
    point1_60 = NXOpen.Point3d(100.00000000000011, 224.22511000881821, 0.0)
    point2_60 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line23, workPart.ModelingViews.WorkView, point1_60, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_60)
    
    point1_61 = NXOpen.Point3d(70.973365829270747, 232.5, 0.0)
    point2_61 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line25, workPart.ModelingViews.WorkView, point1_61, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_61)
    
    dimensionlinearunits511 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits512 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits513 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits514 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits515 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits516 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits517 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits518 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits519 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits520 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits521 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits522 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin14 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin14.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin14.View = NXOpen.View.Null
    assocOrigin14.ViewOfGeometry = workPart.ModelingViews.WorkView
    point45 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin14.PointOnGeometry = point45
    assocOrigin14.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin14.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin14.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.DimensionLine = 0
    assocOrigin14.AssociatedView = NXOpen.View.Null
    assocOrigin14.AssociatedPoint = NXOpen.Point.Null
    assocOrigin14.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin14.XOffsetFactor = 0.0
    assocOrigin14.YOffsetFactor = 0.0
    assocOrigin14.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder18.Origin.SetAssociativeOrigin(assocOrigin14)
    
    point46 = NXOpen.Point3d(81.283372721063543, 217.77225256326568, 0.0)
    sketchRapidDimensionBuilder18.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point46)
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.TextCentered = False
    
    markId168 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject17 = sketchRapidDimensionBuilder18.Commit()
    
    theSession.DeleteUndoMark(markId168, None)
    
    theSession.SetUndoMarkName(markId167, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId167, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder18.Destroy()
    
    markId169 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder19 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines93 = []
    sketchRapidDimensionBuilder19.AppendedText.SetBefore(lines93)
    
    lines94 = []
    sketchRapidDimensionBuilder19.AppendedText.SetAfter(lines94)
    
    lines95 = []
    sketchRapidDimensionBuilder19.AppendedText.SetAbove(lines95)
    
    lines96 = []
    sketchRapidDimensionBuilder19.AppendedText.SetBelow(lines96)
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder19.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder19.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder19.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId169, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder19.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits523 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits524 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits525 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits526 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits527 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits528 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits529 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits530 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits531 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits532 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder19.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder19.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits533 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits534 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits535 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits536 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits537 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits538 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits539 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits540 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits541 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits542 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    expression62 = workPart.Expressions.FindObject("p21")
    expression62.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId169, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId170 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId170, None)
    
    markId171 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId169, "Edit Driving Value")
    
    point47 = NXOpen.Point3d(64.229392329246181, 285.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(line29, workPart.ModelingViews.WorkView, point47)
    
    point1_62 = NXOpen.Point3d(50.781190552751262, 285.0, 0.0)
    point2_62 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line29, workPart.ModelingViews.WorkView, point1_62, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_62)
    
    point1_63 = NXOpen.Point3d(99.999999999999972, 285.0, 0.0)
    point2_63 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line29, workPart.ModelingViews.WorkView, point1_63, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_63)
    
    dimensionlinearunits543 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits544 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits545 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits546 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits547 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits548 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    point1_64 = NXOpen.Point3d(52.921044648127832, 265.0, 0.0)
    point2_64 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line31, workPart.ModelingViews.WorkView, point1_64, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_64)
    
    point1_65 = NXOpen.Point3d(64.229392329246181, 285.0, 0.0)
    point2_65 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line29, workPart.ModelingViews.WorkView, point1_65, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_65)
    
    point1_66 = NXOpen.Point3d(52.921044648127832, 265.0, 0.0)
    point2_66 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line31, workPart.ModelingViews.WorkView, point1_66, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_66)
    
    point1_67 = NXOpen.Point3d(64.229392329246181, 285.0, 0.0)
    point2_67 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line29, workPart.ModelingViews.WorkView, point1_67, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_67)
    
    point1_68 = NXOpen.Point3d(52.921044648127832, 265.0, 0.0)
    point2_68 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line31, workPart.ModelingViews.WorkView, point1_68, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_68)
    
    dimensionlinearunits549 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits550 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits551 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits552 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits553 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits554 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits555 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits556 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits557 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits558 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits559 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits560 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin15 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin15.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin15.View = NXOpen.View.Null
    assocOrigin15.ViewOfGeometry = workPart.ModelingViews.WorkView
    point48 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin15.PointOnGeometry = point48
    assocOrigin15.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin15.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin15.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin15.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin15.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin15.DimensionLine = 0
    assocOrigin15.AssociatedView = NXOpen.View.Null
    assocOrigin15.AssociatedPoint = NXOpen.Point.Null
    assocOrigin15.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin15.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin15.XOffsetFactor = 0.0
    assocOrigin15.YOffsetFactor = 0.0
    assocOrigin15.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder19.Origin.SetAssociativeOrigin(assocOrigin15)
    
    point49 = NXOpen.Point3d(-3.9865292380233748, 270.77786729458995, 0.0)
    sketchRapidDimensionBuilder19.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point49)
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder19.Style.DimensionStyle.TextCentered = False
    
    markId172 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject18 = sketchRapidDimensionBuilder19.Commit()
    
    theSession.DeleteUndoMark(markId172, None)
    
    theSession.SetUndoMarkName(markId171, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId171, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder19.Destroy()
    
    markId173 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder20 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines97 = []
    sketchRapidDimensionBuilder20.AppendedText.SetBefore(lines97)
    
    lines98 = []
    sketchRapidDimensionBuilder20.AppendedText.SetAfter(lines98)
    
    lines99 = []
    sketchRapidDimensionBuilder20.AppendedText.SetAbove(lines99)
    
    lines100 = []
    sketchRapidDimensionBuilder20.AppendedText.SetBelow(lines100)
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder20.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder20.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder20.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder20.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId173, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder20.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits561 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits562 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits563 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits564 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits565 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits566 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits567 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits568 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits569 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits570 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder20.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder20.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder20.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits571 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits572 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits573 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits574 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits575 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits576 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits577 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits578 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits579 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits580 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    expression63 = workPart.Expressions.FindObject("p22")
    expression63.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId173, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId174 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId174, None)
    
    markId175 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId173, "Edit Driving Value")
    
    point50 = NXOpen.Point3d(50.781190552751269, 303.04215452235258, 0.0)
    sketchRapidDimensionBuilder20.FirstAssociativity.SetValue(line30, workPart.ModelingViews.WorkView, point50)
    
    point1_69 = NXOpen.Point3d(50.781190552751276, 310.0, 0.0)
    point2_69 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder20.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line30, workPart.ModelingViews.WorkView, point1_69, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_69)
    
    point1_70 = NXOpen.Point3d(50.781190552751262, 285.0, 0.0)
    point2_70 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder20.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line30, workPart.ModelingViews.WorkView, point1_70, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_70)
    
    dimensionlinearunits581 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits582 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits583 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits584 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits585 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits586 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    point1_71 = NXOpen.Point3d(25.842089296255679, 310.0, 0.0)
    point2_71 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder20.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line32, workPart.ModelingViews.WorkView, point1_71, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_71)
    
    point1_72 = NXOpen.Point3d(50.781190552751269, 303.04215452235258, 0.0)
    point2_72 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder20.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line30, workPart.ModelingViews.WorkView, point1_72, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_72)
    
    point1_73 = NXOpen.Point3d(25.842089296255679, 310.0, 0.0)
    point2_73 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder20.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line32, workPart.ModelingViews.WorkView, point1_73, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_73)
    
    point1_74 = NXOpen.Point3d(50.781190552751269, 303.04215452235258, 0.0)
    point2_74 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder20.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line30, workPart.ModelingViews.WorkView, point1_74, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_74)
    
    point1_75 = NXOpen.Point3d(25.842089296255679, 310.0, 0.0)
    point2_75 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder20.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line32, workPart.ModelingViews.WorkView, point1_75, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_75)
    
    dimensionlinearunits587 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits588 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits589 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits590 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits591 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits592 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits593 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits594 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits595 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits596 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits597 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits598 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin16 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin16.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin16.View = NXOpen.View.Null
    assocOrigin16.ViewOfGeometry = workPart.ModelingViews.WorkView
    point51 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin16.PointOnGeometry = point51
    assocOrigin16.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin16.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin16.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin16.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin16.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin16.DimensionLine = 0
    assocOrigin16.AssociatedView = NXOpen.View.Null
    assocOrigin16.AssociatedPoint = NXOpen.Point.Null
    assocOrigin16.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin16.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin16.XOffsetFactor = 0.0
    assocOrigin16.YOffsetFactor = 0.0
    assocOrigin16.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder20.Origin.SetAssociativeOrigin(assocOrigin16)
    
    point52 = NXOpen.Point3d(39.80071771394018, 336.68919691701927, 0.0)
    sketchRapidDimensionBuilder20.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point52)
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder20.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder20.Style.DimensionStyle.TextCentered = True
    
    markId176 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject19 = sketchRapidDimensionBuilder20.Commit()
    
    theSession.DeleteUndoMark(markId176, None)
    
    theSession.SetUndoMarkName(markId175, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId175, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder20.Destroy()
    
    markId177 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder21 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines101 = []
    sketchRapidDimensionBuilder21.AppendedText.SetBefore(lines101)
    
    lines102 = []
    sketchRapidDimensionBuilder21.AppendedText.SetAfter(lines102)
    
    lines103 = []
    sketchRapidDimensionBuilder21.AppendedText.SetAbove(lines103)
    
    lines104 = []
    sketchRapidDimensionBuilder21.AppendedText.SetBelow(lines104)
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder21.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder21.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder21.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder21.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId177, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder21.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits599 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits600 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits601 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits602 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits603 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits604 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits605 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits606 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits607 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits608 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder21.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder21.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder21.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits609 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits610 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits611 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits612 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits613 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits614 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits615 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits616 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits617 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits618 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    expression64 = workPart.Expressions.FindObject("p23")
    expression64.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId177, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId178 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId178, None)
    
    markId179 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId177, "Edit Driving Value")
    
    point53 = NXOpen.Point3d(193.2865412402966, 279.87570761442396, 0.0)
    sketchRapidDimensionBuilder21.FirstAssociativity.SetValue(line22, workPart.ModelingViews.WorkView, point53)
    
    point1_76 = NXOpen.Point3d(214.02324592671394, 279.87570761442402, 0.0)
    point2_76 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line22, workPart.ModelingViews.WorkView, point1_76, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_76)
    
    point1_77 = NXOpen.Point3d(151.79926341602908, 279.87570761442402, 0.0)
    point2_77 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line22, workPart.ModelingViews.WorkView, point1_77, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_77)
    
    dimensionlinearunits619 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits620 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits621 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits622 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits623 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits624 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    point1_78 = NXOpen.Point3d(199.99999999999997, 200.00000000000003, 0.0)
    point2_78 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line3, workPart.ModelingViews.WorkView, point1_78, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_78)
    
    point1_79 = NXOpen.Point3d(193.2865412402966, 279.87570761442396, 0.0)
    point2_79 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line22, workPart.ModelingViews.WorkView, point1_79, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_79)
    
    point1_80 = NXOpen.Point3d(199.99999999999997, 200.00000000000003, 0.0)
    point2_80 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line3, workPart.ModelingViews.WorkView, point1_80, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_80)
    
    point1_81 = NXOpen.Point3d(193.2865412402966, 279.87570761442396, 0.0)
    point2_81 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line22, workPart.ModelingViews.WorkView, point1_81, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_81)
    
    point1_82 = NXOpen.Point3d(199.99999999999997, 200.00000000000003, 0.0)
    point2_82 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line3, workPart.ModelingViews.WorkView, point1_82, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_82)
    
    dimensionlinearunits625 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits626 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits627 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits628 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits629 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits630 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits631 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits632 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits633 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits634 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits635 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits636 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin17 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin17.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin17.View = NXOpen.View.Null
    assocOrigin17.ViewOfGeometry = workPart.ModelingViews.WorkView
    point54 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin17.PointOnGeometry = point54
    assocOrigin17.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin17.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin17.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin17.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin17.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin17.DimensionLine = 0
    assocOrigin17.AssociatedView = NXOpen.View.Null
    assocOrigin17.AssociatedPoint = NXOpen.Point.Null
    assocOrigin17.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin17.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin17.XOffsetFactor = 0.0
    assocOrigin17.YOffsetFactor = 0.0
    assocOrigin17.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder21.Origin.SetAssociativeOrigin(assocOrigin17)
    
    point55 = NXOpen.Point3d(296.53226036913685, 218.69408934120176, 0.0)
    sketchRapidDimensionBuilder21.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point55)
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder21.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder21.Style.DimensionStyle.TextCentered = False
    
    markId180 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject20 = sketchRapidDimensionBuilder21.Commit()
    
    theSession.DeleteUndoMark(markId180, None)
    
    theSession.SetUndoMarkName(markId179, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId179, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder21.Destroy()
    
    markId181 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder22 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines105 = []
    sketchRapidDimensionBuilder22.AppendedText.SetBefore(lines105)
    
    lines106 = []
    sketchRapidDimensionBuilder22.AppendedText.SetAfter(lines106)
    
    lines107 = []
    sketchRapidDimensionBuilder22.AppendedText.SetAbove(lines107)
    
    lines108 = []
    sketchRapidDimensionBuilder22.AppendedText.SetBelow(lines108)
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder22.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder22.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder22.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder22.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId181, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder22.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits637 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits638 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits639 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits640 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits641 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits642 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits643 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits644 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits645 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits646 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder22.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder22.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder22.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits647 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits648 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits649 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits650 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits651 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits652 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits653 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits654 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits655 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits656 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    expression65 = workPart.Expressions.FindObject("p24")
    expression65.SetFormula("80")
    
    theSession.SetUndoMarkVisibility(markId181, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId182 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId182, None)
    
    markId183 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId181, "Edit Driving Value")
    
    point56 = NXOpen.Point3d(85.892556610743881, 285.0, 0.0)
    sketchRapidDimensionBuilder22.FirstAssociativity.SetValue(line29, workPart.ModelingViews.WorkView, point56)
    
    point1_83 = NXOpen.Point3d(99.999999999999972, 285.0, 0.0)
    point2_83 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder22.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line29, workPart.ModelingViews.WorkView, point1_83, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_83)
    
    point1_84 = NXOpen.Point3d(45.842089296255693, 285.0, 0.0)
    point2_84 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder22.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line29, workPart.ModelingViews.WorkView, point1_84, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_84)
    
    dimensionlinearunits657 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits658 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits659 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits660 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits661 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits662 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    point1_85 = NXOpen.Point3d(0.0, 200.0, 0.0)
    point2_85 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder22.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line3, workPart.ModelingViews.WorkView, point1_85, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_85)
    
    point1_86 = NXOpen.Point3d(85.892556610743881, 285.0, 0.0)
    point2_86 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder22.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line29, workPart.ModelingViews.WorkView, point1_86, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_86)
    
    point1_87 = NXOpen.Point3d(0.0, 200.0, 0.0)
    point2_87 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder22.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line3, workPart.ModelingViews.WorkView, point1_87, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_87)
    
    point1_88 = NXOpen.Point3d(85.892556610743881, 285.0, 0.0)
    point2_88 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder22.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line29, workPart.ModelingViews.WorkView, point1_88, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_88)
    
    point1_89 = NXOpen.Point3d(0.0, 200.0, 0.0)
    point2_89 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder22.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line3, workPart.ModelingViews.WorkView, point1_89, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_89)
    
    dimensionlinearunits663 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits664 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits665 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits666 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits667 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits668 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits669 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits670 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits671 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits672 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits673 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits674 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin18 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin18.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin18.View = NXOpen.View.Null
    assocOrigin18.ViewOfGeometry = workPart.ModelingViews.WorkView
    point57 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin18.PointOnGeometry = point57
    assocOrigin18.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin18.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin18.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin18.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin18.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin18.DimensionLine = 0
    assocOrigin18.AssociatedView = NXOpen.View.Null
    assocOrigin18.AssociatedPoint = NXOpen.Point.Null
    assocOrigin18.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin18.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin18.XOffsetFactor = 0.0
    assocOrigin18.YOffsetFactor = 0.0
    assocOrigin18.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder22.Origin.SetAssociativeOrigin(assocOrigin18)
    
    point58 = NXOpen.Point3d(-67.132348526644392, 240.81817201166754, 0.0)
    sketchRapidDimensionBuilder22.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point58)
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder22.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder22.Style.DimensionStyle.TextCentered = True
    
    markId184 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject21 = sketchRapidDimensionBuilder22.Commit()
    
    theSession.DeleteUndoMark(markId184, None)
    
    theSession.SetUndoMarkName(markId183, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId183, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder22.Destroy()
    
    markId185 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder23 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines109 = []
    sketchRapidDimensionBuilder23.AppendedText.SetBefore(lines109)
    
    lines110 = []
    sketchRapidDimensionBuilder23.AppendedText.SetAfter(lines110)
    
    lines111 = []
    sketchRapidDimensionBuilder23.AppendedText.SetAbove(lines111)
    
    lines112 = []
    sketchRapidDimensionBuilder23.AppendedText.SetBelow(lines112)
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder23.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder23.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder23.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder23.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId185, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder23.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits675 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits676 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits677 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits678 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits679 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits680 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits681 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits682 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits683 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits684 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder23.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder23.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder23.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits685 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits686 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits687 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits688 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits689 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits690 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits691 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits692 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits693 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits694 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    expression66 = workPart.Expressions.FindObject("p25")
    expression66.SetFormula("80")
    
    theSession.SetUndoMarkVisibility(markId185, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId186 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId186, None)
    
    markId187 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId185, "Edit Driving Value")
    
    point59 = NXOpen.Point3d(199.99999999999997, 178.13327111201451, 0.0)
    sketchRapidDimensionBuilder23.FirstAssociativity.SetValue(line2, workPart.ModelingViews.WorkView, point59)
    
    point1_90 = NXOpen.Point3d(171.79926341602902, 230.00000000000006, 0.0)
    point2_90 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder23.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line16, workPart.ModelingViews.WorkView, point1_90, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_90)
    
    dimensionlinearunits695 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits696 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits697 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits698 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits699 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits700 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin19 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin19.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin19.View = NXOpen.View.Null
    assocOrigin19.ViewOfGeometry = workPart.ModelingViews.WorkView
    point60 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin19.PointOnGeometry = point60
    assocOrigin19.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin19.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin19.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin19.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin19.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin19.DimensionLine = 0
    assocOrigin19.AssociatedView = NXOpen.View.Null
    assocOrigin19.AssociatedPoint = NXOpen.Point.Null
    assocOrigin19.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin19.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin19.XOffsetFactor = 0.0
    assocOrigin19.YOffsetFactor = 0.0
    assocOrigin19.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder23.Origin.SetAssociativeOrigin(assocOrigin19)
    
    point61 = NXOpen.Point3d(186.83368379474402, 220.07684450810589, 0.0)
    sketchRapidDimensionBuilder23.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point61)
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder23.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder23.Style.DimensionStyle.TextCentered = True
    
    markId188 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject22 = sketchRapidDimensionBuilder23.Commit()
    
    theSession.DeleteUndoMark(markId188, None)
    
    theSession.SetUndoMarkName(markId187, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId187, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder23.Destroy()
    
    markId189 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder24 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines113 = []
    sketchRapidDimensionBuilder24.AppendedText.SetBefore(lines113)
    
    lines114 = []
    sketchRapidDimensionBuilder24.AppendedText.SetAfter(lines114)
    
    lines115 = []
    sketchRapidDimensionBuilder24.AppendedText.SetAbove(lines115)
    
    lines116 = []
    sketchRapidDimensionBuilder24.AppendedText.SetBelow(lines116)
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder24.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder24.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder24.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder24.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId189, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder24.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits701 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits702 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits703 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits704 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits705 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits706 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits707 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits708 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits709 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits710 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder24.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder24.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder24.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits711 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits712 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits713 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits714 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits715 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits716 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits717 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits718 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits719 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits720 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    expression67 = workPart.Expressions.FindObject("p26")
    expression67.SetFormula("54")
    
    theSession.SetUndoMarkVisibility(markId189, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId190 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId190, None)
    
    markId191 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId189, "Edit Driving Value")
    
    point62 = NXOpen.Point3d(79.999999999999986, 216.85041578532963, 0.0)
    sketchRapidDimensionBuilder24.FirstAssociativity.SetValue(line25, workPart.ModelingViews.WorkView, point62)
    
    point1_91 = NXOpen.Point3d(79.999999999999986, 200.0, 0.0)
    point2_91 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line25, workPart.ModelingViews.WorkView, point1_91, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_91)
    
    point1_92 = NXOpen.Point3d(79.999999999999972, 260.0, 0.0)
    point2_92 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line25, workPart.ModelingViews.WorkView, point1_92, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_92)
    
    dimensionlinearunits721 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits722 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits723 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits724 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits725 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits726 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    point1_93 = NXOpen.Point3d(0.0, 200.0, 0.0)
    point2_93 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line4, workPart.ModelingViews.WorkView, point1_93, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_93)
    
    point1_94 = NXOpen.Point3d(79.999999999999986, 216.85041578532963, 0.0)
    point2_94 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line25, workPart.ModelingViews.WorkView, point1_94, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_94)
    
    point1_95 = NXOpen.Point3d(0.0, 200.0, 0.0)
    point2_95 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line4, workPart.ModelingViews.WorkView, point1_95, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_95)
    
    point1_96 = NXOpen.Point3d(79.999999999999986, 216.85041578532963, 0.0)
    point2_96 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line25, workPart.ModelingViews.WorkView, point1_96, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_96)
    
    point1_97 = NXOpen.Point3d(0.0, 200.0, 0.0)
    point2_97 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line4, workPart.ModelingViews.WorkView, point1_97, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_97)
    
    dimensionlinearunits727 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits728 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits729 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits730 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits731 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits732 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits733 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits734 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits735 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits736 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits737 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits738 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin20 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin20.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin20.View = NXOpen.View.Null
    assocOrigin20.ViewOfGeometry = workPart.ModelingViews.WorkView
    point63 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin20.PointOnGeometry = point63
    assocOrigin20.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin20.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin20.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin20.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin20.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin20.DimensionLine = 0
    assocOrigin20.AssociatedView = NXOpen.View.Null
    assocOrigin20.AssociatedPoint = NXOpen.Point.Null
    assocOrigin20.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin20.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin20.XOffsetFactor = 0.0
    assocOrigin20.YOffsetFactor = 0.0
    assocOrigin20.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder24.Origin.SetAssociativeOrigin(assocOrigin20)
    
    point64 = NXOpen.Point3d(29.199594767675318, 224.68602839778623, 0.0)
    sketchRapidDimensionBuilder24.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point64)
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder24.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder24.Style.DimensionStyle.TextCentered = False
    
    markId192 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject23 = sketchRapidDimensionBuilder24.Commit()
    
    theSession.DeleteUndoMark(markId192, None)
    
    theSession.SetUndoMarkName(markId191, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId191, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder24.Destroy()
    
    markId193 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder25 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines117 = []
    sketchRapidDimensionBuilder25.AppendedText.SetBefore(lines117)
    
    lines118 = []
    sketchRapidDimensionBuilder25.AppendedText.SetAfter(lines118)
    
    lines119 = []
    sketchRapidDimensionBuilder25.AppendedText.SetAbove(lines119)
    
    lines120 = []
    sketchRapidDimensionBuilder25.AppendedText.SetBelow(lines120)
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder25.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder25.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder25.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder25.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId193, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder25.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits739 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits740 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits741 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits742 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits743 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits744 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits745 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits746 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits747 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits748 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder25.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder25.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder25.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits749 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits750 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits751 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits752 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits753 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits754 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits755 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits756 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits757 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits758 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    perpendicularDimension2 = nXObject23
    point65 = NXOpen.Point3d(28.738676378707307, 222.06225303086632, 0.0)
    sketchRapidDimensionBuilder25.FirstAssociativity.SetValue(perpendicularDimension2, workPart.ModelingViews.WorkView, point65)
    
    point1_98 = NXOpen.Point3d(79.999999999999986, 216.85041578532963, 0.0)
    point2_98 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line25, NXOpen.View.Null, point1_98, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_98)
    
    point1_99 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_99 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_99, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_99)
    
    sketchRapidDimensionBuilder25.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    point1_100 = NXOpen.Point3d(79.999999999999986, 200.0, 0.0)
    point2_100 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line25, workPart.ModelingViews.WorkView, point1_100, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_100)
    
    sketchRapidDimensionBuilder25.Destroy()
    
    theSession.UndoToMark(markId193, None)
    
    theSession.DeleteUndoMark(markId193, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId194 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete35 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId195 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects17 = [NXOpen.TaggedObject.Null] * 1 
    perpendicularDimension3 = nXObject17
    objects17[0] = perpendicularDimension3
    nErrs36 = theSession.UpdateManager.AddObjectsToDeleteList(objects17)
    
    notifyOnDelete36 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id17 = theSession.NewestVisibleUndoMark
    
    nErrs37 = theSession.UpdateManager.DoUpdate(id17)
    
    theSession.DeleteUndoMark(markId194, None)
    
    markId196 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchLinearDimensionBuilder1 = workPart.Sketches.CreateLinearDimensionBuilder(perpendicularDimension2)
    
    sketchLinearDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Inferred
    
    sketchLinearDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId196, "線性尺寸 對話方塊")
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits759 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits760 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Style.OrdinateStyle.DoglegCreationOption = NXOpen.Annotations.OrdinateDoglegCreationOption.No
    
    dimensionlinearunits761 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits762 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits763 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits764 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchLinearDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits765 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits766 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits767 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits768 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits769 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits770 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits771 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits772 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits773 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits774 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits775 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits776 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    markId197 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    theSession.DeleteUndoMark(markId197, None)
    
    markId198 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    sketchLinearDimensionBuilder1.Driving.ExpressionValue.SetFormula("54")
    
    sketchLinearDimensionBuilder1.Driving.ExpressionValue.SetFormula("54")
    
    sketchLinearDimensionBuilder1.Driving.ExpressionMode = NXOpen.Annotations.DrivingValueBuilder.DrivingExpressionMode.KeepExpression
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    nXObject24 = sketchLinearDimensionBuilder1.Commit()
    
    point1_101 = NXOpen.Point3d(54.0, 216.85041578532963, 0.0)
    point2_101 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchLinearDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line25, NXOpen.View.Null, point1_101, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_101)
    
    taggedObject1 = sketchLinearDimensionBuilder1.SecondAssociativity.Value
    
    line34 = taggedObject1
    point1_102 = NXOpen.Point3d(0.0, 200.0, 0.0)
    point2_102 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchLinearDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line34, NXOpen.View.Null, point1_102, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_102)
    
    theSession.SetUndoMarkName(markId198, "線性尺寸 - =")
    
    theSession.SetUndoMarkVisibility(markId198, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.SetUndoMarkVisibility(markId196, None, NXOpen.Session.MarkVisibility.Invisible)
    
    markId199 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin21 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin21.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin21.View = NXOpen.View.Null
    assocOrigin21.ViewOfGeometry = workPart.ModelingViews.WorkView
    point66 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin21.PointOnGeometry = point66
    assocOrigin21.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin21.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin21.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin21.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin21.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin21.DimensionLine = 0
    assocOrigin21.AssociatedView = NXOpen.View.Null
    assocOrigin21.AssociatedPoint = NXOpen.Point.Null
    assocOrigin21.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin21.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin21.XOffsetFactor = 0.0
    assocOrigin21.YOffsetFactor = 0.0
    assocOrigin21.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchLinearDimensionBuilder1.Origin.SetAssociativeOrigin(assocOrigin21)
    
    point67 = NXOpen.Point3d(99.720108279785009, 220.53776289707392, 0.0)
    sketchLinearDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point67)
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchLinearDimensionBuilder1.Style.DimensionStyle.TextCentered = False
    
    dimensionlinearunits777 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits778 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits779 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits780 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits781 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits782 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits783 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits784 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits785 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits786 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits787 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits788 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    theSession.SetUndoMarkName(markId199, "線性尺寸 - 指定位置")
    
    theSession.SetUndoMarkVisibility(markId199, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.SetUndoMarkVisibility(markId196, None, NXOpen.Session.MarkVisibility.Invisible)
    
    markId200 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    perpendicularDimension4 = nXObject24
    perpendicularDimension4.LeaderOrientation = NXOpen.Annotations.LeaderOrientation.FromLeft
    
    perpendicularDimension4.IsOriginCentered = False
    
    nErrs38 = theSession.UpdateManager.DoUpdate(markId199)
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin22 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin22.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin22.View = NXOpen.View.Null
    assocOrigin22.ViewOfGeometry = workPart.ModelingViews.WorkView
    point68 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin22.PointOnGeometry = point68
    assocOrigin22.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin22.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin22.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin22.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin22.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin22.DimensionLine = 0
    assocOrigin22.AssociatedView = NXOpen.View.Null
    assocOrigin22.AssociatedPoint = NXOpen.Point.Null
    assocOrigin22.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin22.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin22.XOffsetFactor = 0.0
    assocOrigin22.YOffsetFactor = 0.0
    assocOrigin22.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchLinearDimensionBuilder1.Origin.SetAssociativeOrigin(assocOrigin22)
    
    point69 = NXOpen.Point3d(-90.178267975046282, 210.39755833977708, 0.0)
    sketchLinearDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point69)
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchLinearDimensionBuilder1.Style.DimensionStyle.TextCentered = False
    
    dimensionlinearunits789 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits790 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits791 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits792 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits793 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits794 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits795 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits796 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits797 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits798 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits799 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits800 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    theSession.SetUndoMarkName(markId200, "線性尺寸 - 指定位置")
    
    theSession.SetUndoMarkVisibility(markId200, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.SetUndoMarkVisibility(markId196, None, NXOpen.Session.MarkVisibility.Invisible)
    
    markId201 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    markId202 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    nXObject25 = sketchLinearDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId202, None)
    
    theSession.SetUndoMarkName(markId196, "線性尺寸")
    
    expression68 = sketchLinearDimensionBuilder1.Driving.ExpressionValue
    sketchLinearDimensionBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId201, None)
    
    theSession.SetUndoMarkVisibility(markId196, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.DeleteUndoMark(markId200, None)
    
    theSession.DeleteUndoMark(markId199, None)
    
    theSession.DeleteUndoMark(markId198, None)
    
    markId203 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId204 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId204, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint34 = NXOpen.Point3d(100.0, 280.0, 0.0)
    endPoint34 = NXOpen.Point3d(100.00000000000016, 200.0, 0.0)
    line23.SetEndpoints(startPoint34, endPoint34)
    
    nErrs39 = theSession.UpdateManager.DoUpdate(markId204)
    
    geoms5 = [NXOpen.SmartObject.Null] * 1 
    geoms5[0] = line23
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms5)
    
    geoms6 = [NXOpen.SmartObject.Null] * 1 
    geoms6[0] = line23
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms6)
    
    geoms7 = [NXOpen.SmartObject.Null] * 1 
    geoms7[0] = line23
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms7)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId205 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete37 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId206 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects18 = [NXOpen.TaggedObject.Null] * 1 
    objects18[0] = line23
    nErrs40 = theSession.UpdateManager.AddObjectsToDeleteList(objects18)
    
    notifyOnDelete38 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id18 = theSession.NewestVisibleUndoMark
    
    nErrs41 = theSession.UpdateManager.DoUpdate(id18)
    
    theSession.DeleteUndoMark(markId205, None)
    
    markId207 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId208 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId208, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    parallelDimension3 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    theSession.UpdateManager.LogForUpdate(parallelDimension3)
    
    startPoint35 = NXOpen.Point3d(69.760412996862627, 280.0, 0.0)
    endPoint35 = NXOpen.Point3d(19.842089296255701, 280.0, 0.0)
    line29.SetEndpoints(startPoint35, endPoint35)
    
    sketchHelpedDimensionalConstraint26 = theSession.ActiveSketch.FindObject("DimensionalConstraint p25")
    sketchHelpedDimensionalConstraint26.Refresh()
    
    sketchHelpedDimensionalConstraint27 = theSession.ActiveSketch.FindObject("DimensionalConstraint p22")
    sketchHelpedDimensionalConstraint27.Refresh()
    
    nErrs42 = theSession.UpdateManager.DoUpdate(markId208)
    
    geoms8 = [NXOpen.SmartObject.Null] * 1 
    geoms8[0] = line29
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms8)
    
    geoms9 = [NXOpen.SmartObject.Null] * 1 
    geoms9[0] = line29
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms9)
    
    geoms10 = [NXOpen.SmartObject.Null] * 1 
    geoms10[0] = line29
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms10)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId209 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId210 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId210, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint36 = NXOpen.Point3d(69.760412996862627, 280.0, 0.0)
    endPoint36 = NXOpen.Point3d(69.760412996862797, 200.0, 0.0)
    line35 = workPart.Curves.CreateLine(startPoint36, endPoint36)
    
    theSession.ActiveSketch.AddGeometry(line35, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_27 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_27.Geometry = line35
    geom1_27.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_27.SplineDefiningPointIndex = 0
    geom2_27 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_27.Geometry = line29
    geom2_27.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_27.SplineDefiningPointIndex = 0
    sketchGeometricConstraint58 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_27, geom2_27)
    
    conGeom1_24 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_24.Geometry = line35
    conGeom1_24.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_24.SplineDefiningPointIndex = 0
    conGeom2_24 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_24.Geometry = line3
    conGeom2_24.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_24.SplineDefiningPointIndex = 0
    help15 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help15.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help15.Point.X = 69.299494607894559
    help15.Point.Y = 200.0
    help15.Point.Z = 0.0
    help15.Parameter = 0.0
    sketchHelpedGeometricConstraint17 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_24, conGeom2_24, help15)
    
    geom27 = NXOpen.Sketch.ConstraintGeometry()
    
    geom27.Geometry = line35
    geom27.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom27.SplineDefiningPointIndex = 0
    sketchGeometricConstraint59 = theSession.ActiveSketch.CreateVerticalConstraint(geom27)
    
    dimObject1_32 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_32.Geometry = line35
    dimObject1_32.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_32.AssocValue = 0
    dimObject1_32.HelpPoint.X = 0.0
    dimObject1_32.HelpPoint.Y = 0.0
    dimObject1_32.HelpPoint.Z = 0.0
    dimObject1_32.View = NXOpen.NXObject.Null
    dimObject2_30 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_30.Geometry = line35
    dimObject2_30.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_30.AssocValue = 0
    dimObject2_30.HelpPoint.X = 0.0
    dimObject2_30.HelpPoint.Y = 0.0
    dimObject2_30.HelpPoint.Z = 0.0
    dimObject2_30.View = NXOpen.NXObject.Null
    dimOrigin32 = NXOpen.Point3d(85.438896779082555, 240.00000000000003, 0.0)
    sketchDimensionalConstraint32 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_32, dimObject2_30, dimOrigin32, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint28 = sketchDimensionalConstraint32
    dimension32 = sketchHelpedDimensionalConstraint28.AssociatedDimension
    
    expression69 = sketchHelpedDimensionalConstraint28.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->草圖約束(K)->尺寸(D)->快速(P)...
    # ----------------------------------------------
    markId211 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder26 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines121 = []
    sketchRapidDimensionBuilder26.AppendedText.SetBefore(lines121)
    
    lines122 = []
    sketchRapidDimensionBuilder26.AppendedText.SetAfter(lines122)
    
    lines123 = []
    sketchRapidDimensionBuilder26.AppendedText.SetAbove(lines123)
    
    lines124 = []
    sketchRapidDimensionBuilder26.AppendedText.SetBelow(lines124)
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder26.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder26.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines125 = []
    sketchRapidDimensionBuilder26.AppendedText.SetBefore(lines125)
    
    lines126 = []
    sketchRapidDimensionBuilder26.AppendedText.SetAfter(lines126)
    
    lines127 = []
    sketchRapidDimensionBuilder26.AppendedText.SetAbove(lines127)
    
    lines128 = []
    sketchRapidDimensionBuilder26.AppendedText.SetBelow(lines128)
    
    theSession.SetUndoMarkName(markId211, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder26.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits801 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits802 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits803 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits804 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits805 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits806 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits807 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits808 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits809 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits810 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder26.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder26.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder26.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits811 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits812 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits813 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits814 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits815 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits816 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits817 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits818 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits819 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits820 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    point70 = NXOpen.Point3d(69.760412996862755, 217.31133417429763, 0.0)
    sketchRapidDimensionBuilder26.FirstAssociativity.SetValue(line35, workPart.ModelingViews.WorkView, point70)
    
    point1_103 = NXOpen.Point3d(69.760412996862797, 200.0, 0.0)
    point2_103 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder26.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line35, workPart.ModelingViews.WorkView, point1_103, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_103)
    
    point1_104 = NXOpen.Point3d(69.760412996862627, 280.0, 0.0)
    point2_104 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder26.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line35, workPart.ModelingViews.WorkView, point1_104, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_104)
    
    dimensionlinearunits821 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits822 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits823 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits824 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits825 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits826 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    point1_105 = NXOpen.Point3d(54.0, 230.0, 0.0)
    point2_105 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder26.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line25, workPart.ModelingViews.WorkView, point1_105, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_105)
    
    point1_106 = NXOpen.Point3d(69.760412996862755, 217.31133417429763, 0.0)
    point2_106 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder26.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line35, workPart.ModelingViews.WorkView, point1_106, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_106)
    
    point1_107 = NXOpen.Point3d(54.0, 230.0, 0.0)
    point2_107 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder26.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line25, workPart.ModelingViews.WorkView, point1_107, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_107)
    
    point1_108 = NXOpen.Point3d(69.760412996862755, 217.31133417429763, 0.0)
    point2_108 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder26.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line35, workPart.ModelingViews.WorkView, point1_108, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_108)
    
    point1_109 = NXOpen.Point3d(54.0, 230.0, 0.0)
    point2_109 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder26.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line25, workPart.ModelingViews.WorkView, point1_109, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_109)
    
    dimensionlinearunits827 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits828 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits829 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits830 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits831 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits832 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits833 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits834 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits835 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits836 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits837 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits838 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin23 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin23.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin23.View = NXOpen.View.Null
    assocOrigin23.ViewOfGeometry = workPart.ModelingViews.WorkView
    point71 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin23.PointOnGeometry = point71
    assocOrigin23.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin23.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin23.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin23.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin23.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin23.DimensionLine = 0
    assocOrigin23.AssociatedView = NXOpen.View.Null
    assocOrigin23.AssociatedPoint = NXOpen.Point.Null
    assocOrigin23.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin23.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin23.XOffsetFactor = 0.0
    assocOrigin23.YOffsetFactor = 0.0
    assocOrigin23.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder26.Origin.SetAssociativeOrigin(assocOrigin23)
    
    point72 = NXOpen.Point3d(59.620208439565758, 308.11225680100097, 0.0)
    sketchRapidDimensionBuilder26.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point72)
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder26.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder26.Style.DimensionStyle.TextCentered = True
    
    markId212 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject26 = sketchRapidDimensionBuilder26.Commit()
    
    theSession.DeleteUndoMark(markId212, None)
    
    theSession.SetUndoMarkName(markId211, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId211, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder26.Destroy()
    
    markId213 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder27 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines129 = []
    sketchRapidDimensionBuilder27.AppendedText.SetBefore(lines129)
    
    lines130 = []
    sketchRapidDimensionBuilder27.AppendedText.SetAfter(lines130)
    
    lines131 = []
    sketchRapidDimensionBuilder27.AppendedText.SetAbove(lines131)
    
    lines132 = []
    sketchRapidDimensionBuilder27.AppendedText.SetBelow(lines132)
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder27.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder27.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder27.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder27.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId213, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder27.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits839 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits840 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits841 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits842 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits843 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits844 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits845 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits846 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits847 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits848 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder27.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder27.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder27.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits849 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits850 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits851 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits852 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits853 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits854 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits855 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits856 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits857 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits858 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    expression70 = workPart.Expressions.FindObject("p28")
    expression70.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId213, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId214 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId214, None)
    
    markId215 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId213, "Edit Driving Value")
    
    sketchRapidDimensionBuilder27.Destroy()
    
    theSession.UndoToMark(markId215, None)
    
    theSession.DeleteUndoMark(markId215, None)
    
    sketchRapidDimensionBuilder27.Destroy()
    
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = -0.60107966370838994
    rotMatrix11.Xy = -0.26616526544617197
    rotMatrix11.Xz = 0.75356438964840755
    rotMatrix11.Yx = 0.5131554187812899
    rotMatrix11.Yy = 0.59432081513785651
    rotMatrix11.Yz = 0.61923685684015395
    rotMatrix11.Zx = -0.61267834468961579
    rotMatrix11.Zy = 0.75890633161401633
    rotMatrix11.Zz = -0.22065000744289506
    translation11 = NXOpen.Point3d(70.75534800319582, -284.70702698300033, -133.8079271111319)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 0.5740350996316641)
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    sketch5 = theSession.ActiveSketch
    
    markId216 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId217 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder3.Section = section3
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression71 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder3.DistanceTolerance = 0.01
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies8 = [NXOpen.Body.Null] * 1 
    targetBodies8[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies8)
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("150")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies9 = [NXOpen.Body.Null] * 1 
    targetBodies9[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies9)
    
    extrudeBuilder3.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder3.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder3 = extrudeBuilder3.SmartVolumeProfile
    
    smartVolumeProfileBuilder3.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder3.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId217, "拉伸 對話方塊")
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    section3.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId218 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId219 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features2 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature2 = feature5
    features2[0] = sketchFeature2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2)
    
    section3.AllowSelfIntersection(True)
    
    rules3 = [None] * 1 
    rules3[0] = curveFeatureRule2
    helpPoint3 = NXOpen.Point3d(128.92543915144938, 280.00000000000074, 7.1054273576010019e-14)
    section3.AddToSection(rules3, line22, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId219, None)
    
    direction5 = workPart.Directions.CreateDirection(sketch5, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder3.Direction = direction5
    
    theSession.DeleteUndoMark(markId218, None)
    
    rotMatrix12 = NXOpen.Matrix3x3()
    
    rotMatrix12.Xx = -0.22154044243172075
    rotMatrix12.Xy = -0.89480101628078068
    rotMatrix12.Xz = 0.38762220476907988
    rotMatrix12.Yx = 0.78829826490765675
    rotMatrix12.Yy = 0.069655887177486178
    rotMatrix12.Yz = 0.61133779772323815
    rotMatrix12.Zx = -0.57402585125648897
    rotMatrix12.Zy = 0.44099795764198624
    rotMatrix12.Zz = 0.68993849250847228
    translation12 = NXOpen.Point3d(385.3843046866175, -174.59752831278951, -37.3006755034178)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix12, translation12, 0.29390597101141169)
    
    rotMatrix13 = NXOpen.Matrix3x3()
    
    rotMatrix13.Xx = -0.85666521484505642
    rotMatrix13.Xy = 0.043478404696018901
    rotMatrix13.Xz = 0.51403729242105134
    rotMatrix13.Yx = 0.19176041626049223
    rotMatrix13.Yy = 0.95188021475254814
    rotMatrix13.Yz = 0.23906484375217252
    rotMatrix13.Zx = -0.47890777027532028
    rotMatrix13.Zy = 0.30337054090293175
    rotMatrix13.Zz = -0.82378010566060078
    translation13 = NXOpen.Point3d(277.27467183316907, -276.29895279493587, -21.596897499004271)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix13, translation13, 0.29390597101141169)
    
    direction6 = extrudeBuilder3.Direction
    
    success1 = direction6.ReverseDirection()
    
    extrudeBuilder3.Direction = direction6
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("240")
    
    rotMatrix14 = NXOpen.Matrix3x3()
    
    rotMatrix14.Xx = 0.89688554234995033
    rotMatrix14.Xy = -0.26536589018784451
    rotMatrix14.Xz = 0.35380399693679754
    rotMatrix14.Yx = 0.15065078260000159
    rotMatrix14.Yy = 0.93545574723850533
    rotMatrix14.Yz = 0.31972939599051931
    rotMatrix14.Zx = -0.4158132581167247
    rotMatrix14.Zy = -0.23345982370264112
    rotMatrix14.Zz = 0.87897431423852868
    translation14 = NXOpen.Point3d(191.5060405326214, -270.30288994411421, 63.851561577372728)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix14, translation14, 0.29390597101141169)
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("30")
    
    rotMatrix15 = NXOpen.Matrix3x3()
    
    rotMatrix15.Xx = -0.78647827970745021
    rotMatrix15.Xy = -0.27569318442607033
    rotMatrix15.Xz = 0.55267095419374457
    rotMatrix15.Yx = -0.019677018023391092
    rotMatrix15.Yy = 0.90557342695342424
    rotMatrix15.Yz = 0.42373291512170769
    rotMatrix15.Zx = -0.61730440668289333
    rotMatrix15.Zy = 0.32238181781366781
    rotMatrix15.Zz = -0.71763865073798683
    translation15 = NXOpen.Point3d(325.510629378857, -251.88749160689719, -13.924415348755431)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix15, translation15, 0.29390597101141169)
    
    extrudeBuilder3.Destroy()
    
    section3.Destroy()
    
    workPart.Expressions.Delete(expression71)
    
    theSession.UndoToMark(markId217, None)
    
    theSession.DeleteUndoMark(markId217, None)
    
    scaleAboutPoint47 = NXOpen.Point3d(229.55896325556563, -110.72844109974349, 0.0)
    viewCenter47 = NXOpen.Point3d(-229.55896325556563, 110.72844109974342, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(286.94870406945699, -136.15997330354628, 0.0)
    viewCenter48 = NXOpen.Point3d(-286.94870406945699, 136.15997330354611, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(358.68588008682121, -167.38674404051665, 0.0)
    viewCenter49 = NXOpen.Point3d(-358.68588008682121, 167.38674404051639, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(448.35735010852642, -196.92558122413715, 0.0)
    viewCenter50 = NXOpen.Point3d(-448.35735010852642, 196.92558122413683, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(358.6858800868211, -157.54046497930972, 0.0)
    viewCenter51 = NXOpen.Point3d(-358.6858800868211, 157.54046497930946, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(286.94870406945671, -126.03237198344766, 0.0)
    viewCenter52 = NXOpen.Point3d(-286.94870406945705, 126.03237198344758, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(229.5589632555654, -100.8258975867583, 0.0)
    viewCenter53 = NXOpen.Point3d(-229.55896325556569, 100.82589758675807, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(183.64717060445227, -80.660718069406627, 0.0)
    viewCenter54 = NXOpen.Point3d(-183.64717060445253, 80.660718069406443, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint54, viewCenter54)
    
    markId220 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Enter Direct Sketch")
    
    theSession.SetUndoMarkVisibility(markId220, "Enter Direct Sketch", NXOpen.Session.MarkVisibility.Visible)
    
    sketch5.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId221 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId222 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId222, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint37 = NXOpen.Point3d(145.99999999999991, 200.0, 0.0)
    endPoint37 = NXOpen.Point3d(125.99999999999993, 200.0, 0.0)
    line36 = workPart.Curves.CreateLine(startPoint37, endPoint37)
    
    theSession.ActiveSketch.AddGeometry(line36, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_28 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_28.Geometry = line36
    geom1_28.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_28.SplineDefiningPointIndex = 0
    geom2_28 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_28.Geometry = line16
    geom2_28.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_28.SplineDefiningPointIndex = 0
    sketchGeometricConstraint60 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_28, geom2_28)
    
    geom28 = NXOpen.Sketch.ConstraintGeometry()
    
    geom28.Geometry = line36
    geom28.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom28.SplineDefiningPointIndex = 0
    sketchGeometricConstraint61 = theSession.ActiveSketch.CreateHorizontalConstraint(geom28)
    
    geom1_29 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_29.Geometry = line36
    geom1_29.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_29.SplineDefiningPointIndex = 0
    geom2_29 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_29.Geometry = line33
    geom2_29.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_29.SplineDefiningPointIndex = 0
    sketchGeometricConstraint62 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_29, geom2_29)
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->直線(L)...
    # ----------------------------------------------
    markId223 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId224 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId224, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint38 = NXOpen.Point3d(73.999999999999972, 200.0, 0.0)
    endPoint38 = NXOpen.Point3d(52.98699778072924, 200.0, 0.0)
    line37 = workPart.Curves.CreateLine(startPoint38, endPoint38)
    
    theSession.ActiveSketch.AddGeometry(line37, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_30 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_30.Geometry = line37
    geom1_30.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_30.SplineDefiningPointIndex = 0
    geom2_30 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_30.Geometry = line35
    geom2_30.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_30.SplineDefiningPointIndex = 0
    sketchGeometricConstraint63 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_30, geom2_30)
    
    geom29 = NXOpen.Sketch.ConstraintGeometry()
    
    geom29.Geometry = line37
    geom29.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom29.SplineDefiningPointIndex = 0
    sketchGeometricConstraint64 = theSession.ActiveSketch.CreateHorizontalConstraint(geom29)
    
    conGeom1_25 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_25.Geometry = line37
    conGeom1_25.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_25.SplineDefiningPointIndex = 0
    conGeom2_25 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_25.Geometry = line3
    conGeom2_25.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_25.SplineDefiningPointIndex = 0
    help16 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help16.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help16.Point.X = 52.98699778072924
    help16.Point.Y = 200.0
    help16.Point.Z = 0.0
    help16.Parameter = 0.0
    sketchHelpedGeometricConstraint18 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_25, conGeom2_25, help16)
    
    dimObject1_33 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_33.Geometry = line37
    dimObject1_33.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_33.AssocValue = 0
    dimObject1_33.HelpPoint.X = 0.0
    dimObject1_33.HelpPoint.Y = 0.0
    dimObject1_33.HelpPoint.Z = 0.0
    dimObject1_33.View = NXOpen.NXObject.Null
    dimObject2_31 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_31.Geometry = line37
    dimObject2_31.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_31.AssocValue = 0
    dimObject2_31.HelpPoint.X = 0.0
    dimObject2_31.HelpPoint.Y = 0.0
    dimObject2_31.HelpPoint.Z = 0.0
    dimObject2_31.View = NXOpen.NXObject.Null
    dimOrigin33 = NXOpen.Point3d(63.493498890364606, 189.96060583151271, 0.0)
    sketchDimensionalConstraint33 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_33, dimObject2_31, dimOrigin33, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint29 = sketchDimensionalConstraint33
    dimension33 = sketchHelpedDimensionalConstraint29.AssociatedDimension
    
    expression72 = sketchHelpedDimensionalConstraint29.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    scaleAboutPoint55 = NXOpen.Point3d(38.368147620769726, -66.406409343639936, 0.0)
    viewCenter55 = NXOpen.Point3d(-38.368147620769726, 66.406409343639965, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(47.22233553325502, -83.008011679549881, 0.0)
    viewCenter56 = NXOpen.Point3d(-47.22233553325502, 83.008011679549909, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint56, viewCenter56)
    
    scaleAboutPoint57 = NXOpen.Point3d(59.027919416568771, -103.76001459943738, 0.0)
    viewCenter57 = NXOpen.Point3d(-59.027919416568771, 103.76001459943738, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(73.784899270710966, -129.12357372374427, 0.0)
    viewCenter58 = NXOpen.Point3d(-73.784899270710966, 129.12357372374427, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(91.510568431448192, -162.12502281162088, 0.0)
    viewCenter59 = NXOpen.Point3d(-91.510568431448192, 162.12502281162088, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(73.208454745158548, -130.85290730040154, 0.0)
    viewCenter60 = NXOpen.Point3d(-73.208454745158548, 130.8529073004016, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(58.56676379612685, -104.68232584032121, 0.0)
    viewCenter61 = NXOpen.Point3d(-58.56676379612685, 104.68232584032124, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(46.853411036901477, -83.745860672256995, 0.0)
    viewCenter62 = NXOpen.Point3d(-46.853411036901477, 83.745860672257024, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(37.482728829521186, -66.996688537805582, 0.0)
    viewCenter63 = NXOpen.Point3d(-37.482728829521186, 66.996688537805625, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(29.750071385950683, -53.597350830244501, 0.0)
    viewCenter64 = NXOpen.Point3d(-29.750071385950726, 53.59735083024448, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(15.111147370641564, -48.355671586053198, 0.0)
    viewCenter65 = NXOpen.Point3d(-15.111147370641628, 48.355671586053134, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(11.937806422806842, -38.835648742548976, 0.0)
    viewCenter66 = NXOpen.Point3d(-11.937806422806894, 38.835648742548926, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(9.5502451382454758, -31.068518994039199, 0.0)
    viewCenter67 = NXOpen.Point3d(-9.5502451382455167, 31.068518994039145, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(7.6401961105963796, -24.854815195231364, 0.0)
    viewCenter68 = NXOpen.Point3d(-7.6401961105964213, 24.854815195231303, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(5.8026805903263545, -17.021196398290741, 0.0)
    viewCenter69 = NXOpen.Point3d(-5.8026805903264078, 17.021196398290687, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(4.7040397318912284, -13.431271339742151, 0.0)
    viewCenter70 = NXOpen.Point3d(-4.7040397318912595, 13.431271339742095, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(3.763231785512982, -10.645984656385494, 0.0)
    viewCenter71 = NXOpen.Point3d(-3.7632317855130162, 10.645984656385435, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint71, viewCenter71)
    
    markId225 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId225, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint39 = NXOpen.Point3d(55.152606242883493, 200.0, 0.0)
    endPoint39 = NXOpen.Point3d(57.885900908150838, 200.0, 0.0)
    line38 = workPart.Curves.CreateLine(startPoint39, endPoint39)
    
    theSession.ActiveSketch.AddGeometry(line38, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_26 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_26.Geometry = line38
    conGeom1_26.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_26.SplineDefiningPointIndex = 0
    conGeom2_26 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_26.Geometry = line37
    conGeom2_26.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_26.SplineDefiningPointIndex = 0
    help17 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help17.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help17.Point.X = 55.152606242883493
    help17.Point.Y = 200.0
    help17.Point.Z = 0.0
    help17.Parameter = 0.0
    sketchHelpedGeometricConstraint19 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_26, conGeom2_26, help17)
    
    geom30 = NXOpen.Sketch.ConstraintGeometry()
    
    geom30.Geometry = line38
    geom30.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom30.SplineDefiningPointIndex = 0
    sketchGeometricConstraint65 = theSession.ActiveSketch.CreateHorizontalConstraint(geom30)
    
    conGeom1_27 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_27.Geometry = line38
    conGeom1_27.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_27.SplineDefiningPointIndex = 0
    conGeom2_27 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_27.Geometry = line37
    conGeom2_27.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_27.SplineDefiningPointIndex = 0
    help18 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help18.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help18.Point.X = 57.885900908150838
    help18.Point.Y = 200.0
    help18.Point.Z = 0.0
    help18.Parameter = 0.0
    sketchHelpedGeometricConstraint20 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_27, conGeom2_27, help18)
    
    dimObject1_34 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_34.Geometry = line38
    dimObject1_34.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_34.AssocValue = 0
    dimObject1_34.HelpPoint.X = 0.0
    dimObject1_34.HelpPoint.Y = 0.0
    dimObject1_34.HelpPoint.Z = 0.0
    dimObject1_34.View = NXOpen.NXObject.Null
    dimObject2_32 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_32.Geometry = line38
    dimObject2_32.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_32.AssocValue = 0
    dimObject2_32.HelpPoint.X = 0.0
    dimObject2_32.HelpPoint.Y = 0.0
    dimObject2_32.HelpPoint.Z = 0.0
    dimObject2_32.View = NXOpen.NXObject.Null
    dimOrigin34 = NXOpen.Point3d(56.519253575517169, 201.3474646757908, 0.0)
    sketchDimensionalConstraint34 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_34, dimObject2_32, dimOrigin34, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint30 = sketchDimensionalConstraint34
    dimension34 = sketchHelpedDimensionalConstraint30.AssociatedDimension
    
    expression73 = sketchHelpedDimensionalConstraint30.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   對話開始 直線
    # ----------------------------------------------
    scaleAboutPoint72 = NXOpen.Point3d(-6.8530431462500099, -3.0105854284104301, 0.0)
    viewCenter72 = NXOpen.Point3d(6.8530431462499788, 3.0105854284103728, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(-8.5663039328125112, -3.4661345392883178, 0.0)
    viewCenter73 = NXOpen.Point3d(8.5663039328124775, 3.4661345392882588, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(-10.707879916015626, -4.0850871355897969, 0.0)
    viewCenter74 = NXOpen.Point3d(10.707879916015605, 4.0850871355897391, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint74, viewCenter74)
    
    scaleAboutPoint75 = NXOpen.Point3d(-13.462218969557211, -4.7195135467988099, 0.0)
    viewCenter75 = NXOpen.Point3d(13.462218969557185, 4.7195135467987566, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(-16.827773711946509, -5.5125465608100823, 0.0)
    viewCenter76 = NXOpen.Point3d(16.827773711946492, 5.5125465608100246, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint76, viewCenter76)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId226 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder4 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section4 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder4.Section = section4
    
    extrudeBuilder4.AllowSelfIntersectingSection(True)
    
    expression74 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder4.DistanceTolerance = 0.01
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies10 = [NXOpen.Body.Null] * 1 
    targetBodies10[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies10)
    
    extrudeBuilder4.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("150")
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies11 = [NXOpen.Body.Null] * 1 
    targetBodies11[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies11)
    
    extrudeBuilder4.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder4.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder4 = extrudeBuilder4.SmartVolumeProfile
    
    smartVolumeProfileBuilder4.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder4.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId226, "拉伸 對話方塊")
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    section4.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId227 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves3 = [NXOpen.ICurve.Null] * 17 
    curves3[0] = line30
    curves3[1] = line20
    curves3[2] = line27
    curves3[3] = line37
    curves3[4] = line31
    curves3[5] = line16
    curves3[6] = line18
    curves3[7] = line22
    curves3[8] = line36
    curves3[9] = line19
    curves3[10] = line32
    curves3[11] = line17
    curves3[12] = line35
    curves3[13] = line25
    curves3[14] = line29
    curves3[15] = line38
    curves3[16] = line33
    seedPoint3 = NXOpen.Point3d(24.561392864170472, 266.66666666666669, 0.0)
    regionBoundaryRule3 = workPart.ScRuleFactory.CreateRuleRegionBoundary(theSession.ActiveSketch, curves3, seedPoint3, 0.01)
    
    curves4 = [NXOpen.ICurve.Null] * 17 
    curves4[0] = line30
    curves4[1] = line20
    curves4[2] = line27
    curves4[3] = line37
    curves4[4] = line31
    curves4[5] = line16
    curves4[6] = line18
    curves4[7] = line22
    curves4[8] = line36
    curves4[9] = line19
    curves4[10] = line32
    curves4[11] = line17
    curves4[12] = line35
    curves4[13] = line25
    curves4[14] = line29
    curves4[15] = line38
    curves4[16] = line33
    seedPoint4 = NXOpen.Point3d(201.55731584401823, 280.0, 0.0)
    regionBoundaryRule4 = workPart.ScRuleFactory.CreateRuleRegionBoundary(theSession.ActiveSketch, curves4, seedPoint4, 0.01)
    
    section4.AllowSelfIntersection(True)
    
    rules4 = [None] * 2 
    rules4[0] = regionBoundaryRule3
    rules4[1] = regionBoundaryRule4
    helpPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section4.AddToSection(rules4, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint4, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId227, None)
    
    markId228 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId229 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId229, None)
    
    direction7 = workPart.Directions.CreateDirection(theSession.ActiveSketch, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder4.Direction = direction7
    
    expression75 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression76 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId228, None)
    
    scaleAboutPoint77 = NXOpen.Point3d(-53.191238744658449, 16.44092833925804, 0.0)
    viewCenter77 = NXOpen.Point3d(53.191238744658449, -16.4409283392581, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(-66.489048430823061, 20.55116042407256, 0.0)
    viewCenter78 = NXOpen.Point3d(66.489048430823061, -20.551160424072609, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(-83.111310538528826, 25.688950530090697, 0.0)
    viewCenter79 = NXOpen.Point3d(83.111310538528826, -25.688950530090761, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(-103.889138173161, 32.111188162613388, 0.0)
    viewCenter80 = NXOpen.Point3d(103.889138173161, -32.111188162613452, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    scaleAboutPoint81 = NXOpen.Point3d(-129.86142271645124, 39.843845606183905, 0.0)
    viewCenter81 = NXOpen.Point3d(129.86142271645124, -39.843845606183905, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint81, viewCenter81)
    
    scaleAboutPoint82 = NXOpen.Point3d(-162.32677839556408, 49.066958015022813, 0.0)
    viewCenter82 = NXOpen.Point3d(162.32677839556408, -49.066958015022777, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint82, viewCenter82)
    
    scaleAboutPoint83 = NXOpen.Point3d(-202.44731737401315, 58.566763796126821, 0.0)
    viewCenter83 = NXOpen.Point3d(202.44731737401315, -58.566763796126821, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint83, viewCenter83)
    
    rotMatrix16 = NXOpen.Matrix3x3()
    
    rotMatrix16.Xx = 0.24341883369830994
    rotMatrix16.Xy = -0.315708279957152
    rotMatrix16.Xz = 0.91710171375232497
    rotMatrix16.Yx = 0.48691816317101017
    rotMatrix16.Yy = 0.85753521003251565
    rotMatrix16.Yz = 0.16596405010922827
    rotMatrix16.Zx = -0.83884323551848694
    rotMatrix16.Zy = 0.4061547063878313
    rotMatrix16.Zz = 0.36246431645596588
    translation16 = NXOpen.Point3d(-206.2096203643959, -166.7487511286873, 1.1770647342173675)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix16, translation16, 0.45899183981281227)
    
    direction8 = extrudeBuilder4.Direction
    
    success2 = direction8.ReverseDirection()
    
    extrudeBuilder4.Direction = direction8
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("70")
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("30")
    
    rotMatrix17 = NXOpen.Matrix3x3()
    
    rotMatrix17.Xx = 0.23378932360777566
    rotMatrix17.Xy = 0.26018183204260742
    rotMatrix17.Xz = 0.93682867507456968
    rotMatrix17.Yx = 0.8313149092910791
    rotMatrix17.Yy = 0.44620817804764296
    rotMatrix17.Yz = -0.3313816280872699
    rotMatrix17.Zx = -0.50424009534881764
    rotMatrix17.Zy = 0.85627313172746344
    rotMatrix17.Zz = -0.11197432796967052
    translation17 = NXOpen.Point3d(-301.86834664252871, -126.26919914763275, -101.81489648520622)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix17, translation17, 0.45899183981281227)
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("7")
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("70")
    
    rotMatrix18 = NXOpen.Matrix3x3()
    
    rotMatrix18.Xx = 0.35597734303605671
    rotMatrix18.Xy = -0.91515275097121951
    rotMatrix18.Xz = -0.18914431959432912
    rotMatrix18.Yx = 0.93418323635398137
    rotMatrix18.Yy = 0.34326896721652322
    rotMatrix18.Yz = 0.097304147194790261
    rotMatrix18.Zx = -0.024120782744203623
    rotMatrix18.Zy = -0.21133352440139291
    rotMatrix18.Zz = 0.97711633355701155
    translation18 = NXOpen.Point3d(-115.09721374917966, -117.51471735896195, 37.385151007554981)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix18, translation18, 0.45899183981281227)
    
    markId230 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId230, None)
    
    markId231 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder4.ParentFeatureInternal = False
    
    markId232 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    try:
        # 工具體完全在目標體外。
        feature6 = extrudeBuilder4.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(670030)
        
    theSession.UndoToMarkWithStatus(markId231, None)
    
    theSession.DeleteUndoMark(markId231, None)
    
    rotMatrix19 = NXOpen.Matrix3x3()
    
    rotMatrix19.Xx = -0.20728682029055168
    rotMatrix19.Xy = 0.68151455492499369
    rotMatrix19.Xz = -0.70183337449798155
    rotMatrix19.Yx = 0.91659959901880106
    rotMatrix19.Yy = 0.38601124674586645
    rotMatrix19.Yz = 0.10411768564599531
    rotMatrix19.Zx = 0.3418732940906743
    rotMatrix19.Zy = -0.62171796564929083
    rotMatrix19.Zz = -0.70469101170406856
    translation19 = NXOpen.Point3d(-297.59627009122499, -123.73384001886379, 202.06066983537403)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix19, translation19, 0.45899183981281261)
    
    markId233 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId233, None)
    
    markId234 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder4.ParentFeatureInternal = False
    
    markId235 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    try:
        # 工具體完全在目標體外。
        feature7 = extrudeBuilder4.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(670030)
        
    theSession.UndoToMarkWithStatus(markId234, None)
    
    theSession.DeleteUndoMark(markId234, None)
    
    rotMatrix20 = NXOpen.Matrix3x3()
    
    rotMatrix20.Xx = -0.44993584829155009
    rotMatrix20.Xy = 0.8157019368523597
    rotMatrix20.Xz = -0.36357679056490361
    rotMatrix20.Yx = -0.88735777812464234
    rotMatrix20.Yy = -0.45427271443157036
    rotMatrix20.Yz = 0.078946022855333198
    rotMatrix20.Zx = -0.10076659180435087
    rotMatrix20.Zy = 0.35814333881601923
    rotMatrix20.Zz = 0.92821303742075056
    translation20 = NXOpen.Point3d(-325.42212342470475, 167.71023558459029, -48.003062744110721)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix20, translation20, 0.45899183981281261)
    
    rotMatrix21 = NXOpen.Matrix3x3()
    
    rotMatrix21.Xx = 0.1593184425050588
    rotMatrix21.Xy = -0.72441760609023464
    rotMatrix21.Xz = -0.67069871467318465
    rotMatrix21.Yx = -0.96234930590147127
    rotMatrix21.Yy = -0.26551538464458008
    rotMatrix21.Yz = 0.05818413828528482
    rotMatrix21.Zx = -0.22023044137612413
    rotMatrix21.Zy = 0.63617663624463516
    rotMatrix21.Zz = -0.73944427794644763
    translation21 = NXOpen.Point3d(-94.702208353643684, 143.83987027758855, 40.360147504386198)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix21, translation21, 0.45899183981281261)
    
    markId236 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId236, None)
    
    markId237 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder4.ParentFeatureInternal = False
    
    markId238 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    try:
        # 工具體完全在目標體外。
        feature8 = extrudeBuilder4.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(670030)
        
    theSession.UndoToMarkWithStatus(markId237, None)
    
    theSession.DeleteUndoMark(markId237, None)
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies12 = [NXOpen.Body.Null] * 1 
    targetBodies12[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies12)
    
    markId239 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId239, None)
    
    markId240 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder4.ParentFeatureInternal = False
    
    markId241 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    feature9 = extrudeBuilder4.CommitFeature()
    
    theSession.DeleteUndoMark(markId240, None)
    
    theSession.SetUndoMarkName(markId226, "拉伸")
    
    expression77 = extrudeBuilder4.Limits.StartExtend.Value
    expression78 = extrudeBuilder4.Limits.EndExtend.Value
    extrudeBuilder4.Destroy()
    
    workPart.Expressions.Delete(expression74)
    
    workPart.Expressions.Delete(expression75)
    
    workPart.Expressions.Delete(expression76)
    
    rotMatrix22 = NXOpen.Matrix3x3()
    
    rotMatrix22.Xx = -0.2630769522815693
    rotMatrix22.Xy = 0.96284909874394542
    rotMatrix22.Xz = 0.060927253558794567
    rotMatrix22.Yx = -0.96283620353507238
    rotMatrix22.Yy = -0.26602571812195014
    rotMatrix22.Yz = 0.046655786992326975
    rotMatrix22.Zx = 0.061130698837927613
    rotMatrix22.Zy = -0.046388903260127762
    rotMatrix22.Zz = 0.99705120596382402
    translation22 = NXOpen.Point3d(-362.93925318695665, 144.83297591885707, -15.056622616137602)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix22, translation22, 0.45899183981281261)
    
    rotMatrix23 = NXOpen.Matrix3x3()
    
    rotMatrix23.Xx = 0.21288692859518085
    rotMatrix23.Xy = 0.30854018263272454
    rotMatrix23.Xz = -0.92708258064440063
    rotMatrix23.Yx = -0.42247949159517284
    rotMatrix23.Yy = 0.88461693747232151
    rotMatrix23.Yz = 0.19739289024324341
    rotMatrix23.Zx = 0.88101659167963431
    rotMatrix23.Zy = 0.34965101120697673
    rotMatrix23.Zz = 0.31867528229711256
    translation23 = NXOpen.Point3d(-238.57237342276181, -98.1602610170128, -109.86973382411774)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix23, translation23, 0.45899183981281261)
    
    rotMatrix24 = NXOpen.Matrix3x3()
    
    rotMatrix24.Xx = -0.22432992836439603
    rotMatrix24.Xy = 0.73799001757022809
    rotMatrix24.Xz = -0.63643288507644313
    rotMatrix24.Yx = 0.31783659713138057
    rotMatrix24.Yy = 0.67277353047033484
    rotMatrix24.Yz = 0.66809855127999962
    rotMatrix24.Zx = 0.92122526059806598
    rotMatrix24.Zy = -0.052407162346204829
    rotMatrix24.Zz = -0.38548347379732145
    translation24 = NXOpen.Point3d(-280.37720344064996, -178.17439626537276, 0.073014452603061386)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix24, translation24, 0.45899183981281261)
    
    # ----------------------------------------------
    #   功能表：工具(T)->動作記錄(J)->停止錄製(S)
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()